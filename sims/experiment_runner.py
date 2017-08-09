from dolfin import MPI, mpi_comm_world
from experiment_db import *
from channel_runner import *
import pprint
from scipy.optimize import minimize_scalar
from sim_constants import *
import numpy as np

"""
Convenience object for doing model runs. Has different logic for steady state
tuning runs and summer runs.
"""

class ExperimentRunner(object):

  def __init__(self):
    self.MPI_rank = MPI.rank(mpi_comm_world())
    self.pp = pprint.PrettyPrinter(indent=4)


  ### Run all steady state simulations
  def run_all_steady(self, experiment_title, tune = True):
    experiment = experiment_db[experiment_title]

    for run_title in experiment.steady_runs.keys():
      self.run(experiment_title, run_title, tune = tune)
      print
      print


  ### Run all winter simulations
  def run_all_winter(self, experiment_title):
    experiment = experiment_db[experiment_title]

    for run_title in experiment.winter_runs.keys():
      self.run(experiment_title, run_title, tune = False)
      print
      print


  ### Run a single experiment
  def run(self, experiment_title, run_title, tune = True):
    run = experiment_db[experiment_title].runs[run_title]

    run_options = run.run_options
    model_inputs = run.model_inputs

    # Print run details
    if self.MPI_rank == 0:
      print "Experiment: " + experiment_title
      print "Run: " + run_title
      print
      self.pp.pprint(model_inputs)
      print
      self.pp.pprint(run_options)
      print

    T = run_options['end_time']
    dt = run_options['dt']

    # Function called prior to each step
    def pre_step(model):
      # Print the average pfo
      avg_pfo = assemble(model.pfo * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
      # Print average sheet height
      avg_h = assemble(model.h * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
      # Print max channel area
      max_S = 0.0
      if model_inputs['use_channels']:
        max_S = model.S.vector().max()

      if self.MPI_rank == 0:
        print "Avg. PFO: " + str(avg_pfo)
        print "Avg. h: " + str(avg_h)
        print "Max S: " + str(max_S)

    # Channel runner object
    channel_runner = ChannelRunner(run, pre_step = pre_step)

    def set_k(k):
      # Update the conductivity. If we allow for variable k then change k_max
      # Otherwise change k_min and k_max so k is constant
      if run_options['vark'] :
        channel_runner.scale_functions.k_max = k
      else :
        channel_runner.scale_functions.k_min = k
        channel_runner.scale_functions.k_max = k

      # Update conductivity
      channel_runner.model.set_k(channel_runner.scale_functions.get_k(0.0))


    if run.is_steady :
      # Steady state output file
      steady_file = model_inputs['steady_file']

      # Set initial sheet height if specified
      if 'h_0' in run_options:
          h_0 = run_options['h_0']
          print "Setting h_0 to: " + str(h_0)
          print
          channel_runner.model.set_h(Constant(h_0))

      if tune:
        ### Tuning steady state run

        # Get target PFO
        target_pfo = run_options['tune_pfo']

        # Objective function
        def f(k):

          if self.MPI_rank == 0:
            print "k: "  + str(k)
            print
            print

          # Update conductivity
          set_k(k)
          # Run simulation for a while
          channel_runner.do_run(channel_runner.model.t + T, dt, steady_file = steady_file)
          # Get average pressure
          avg_pfo = assemble(channel_runner.model.pfo * dx(channel_runner.model.mesh)) / assemble(1.0 * dx(channel_runner.model.mesh))
          # Compute error
          err = abs(avg_pfo - target_pfo)

          if self.MPI_rank == 0:
            print
            print "Error: " + str(err)
            print

          # Error tolerance is finicky and difficult to choose for this method
          # so if error is small enough, call it good and break prematurely
          if err <= 0.01:
            # Write out a file with the tuned conductivity value
            print "Tuned k: " + str(k)
            np.savetxt(model_inputs['out_dir'] + '/' + run_title + '_tune.txt', np.array([k]))
            sys.exit(1)

          return err

        # Do the optimization
        options = {}
        options['maxiter'] = 20
        options['disp'] = True

        if self.MPI_rank == 0:
          print "Bounds: "
          print (run_options['k_bound_low'], run_options['k_bound_high'])
          print

        res = minimize_scalar(f, bounds=(run_options['k_bound_low'], run_options['k_bound_high']), method='bounded', tol = run_options['tune_atol'], options = options)

        if self.MPI_rank == 0:
          print "Tuned k: " + str(res.x)

        # Write out a file with the tuned conductivity value
        np.savetxt(model_inputs['out_dir'] + '/' + run_title + '_tune.txt', np.array([res.x]))

      else :
        ### Non-tuning steady state run

        # Update conductivity
        set_k(run_options['scale_k_max'])
        # Run simulation
        channel_runner.do_run(T, dt, steady_file = steady_file)

    else :
      ### Winter run

      # Update conductivity
      set_k(run_options['scale_k_max'])
      # Run simulation
      channel_runner.do_run(T, dt)
