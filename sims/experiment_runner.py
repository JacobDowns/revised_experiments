## Encapsulates a single model run
from dolfin import MPI, mpi_comm_world
from experiment_db import *
from channel_runner import *
import pprint
from scipy.optimize import minimize_scalar
s#et_log_level(30)

class ExperimentRunner(object):

  def __init__(self):
    self.MPI_rank = MPI.rank(mpi_comm_world())
    self.pp = pprint.PrettyPrinter(indent=4)
  

  ### Run a single experiment  
  def run(self, experiment_title, run_title):
    run = experiment_db[experiment_title].runs[run_title]
    
    run_options = run.run_options
    model_inputs = run.model_inputs
    
    if self.MPI_rank == 0:
      print "Experiment: " + experiment_title 
      print "Run: " + run_title
      print
      self.pp.pprint(model_inputs) 
      print
      self.pp.pprint(run_options)
      print
      
    T = run_options['end_time']
    
    # Function called prior to each step
    def pre_step(model):
      # Print the average pfo    
      avg_pfo = assemble(model.pfo * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
      # Print average water height
      avg_h = assemble(model.h * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
      
      if self.MPI_rank == 0:
        print "Avg. PFO: " + str(avg_pfo)
        print "Avg. h: " + str(avg_h)
        print


    # Channel runner object
    channel_runner = ChannelRunner(model_inputs, run_options, pre_step = pre_step)
    

    if run.is_steady :
      ### For a steady state run, automatically tune pressure using simplex method
    
      # Get target PFO
      target_pfo = run_options['tune_pfo']
      # Steady state output file
      steady_file = model_inputs['steady_file']

      # Objective function   
      def f(k):
        
        if self.MPI_rank == 0:
          print "k: "  + str(k)
          print
        
        
        # Update the conductivity. If we allow for variable k then change k_max
        # Otherwise change k_min and k_max so k is constant
        
        if run_options['vark'] :
          channel_runner.scale_functions.k_max = k
        else :
          channel_runner.scale_functions.k_min = k
          channel_runner.scale_functions.k_max = k
       
        channel_runner.model.set_k(channel_runner.scale_functions.get_k(0.0))
        
       
        # Run simulation for a while
        channel_runner.run(channel_runner.model.t + T, dt, steady_file = steady_file)
        
        
        # Return average pressure
        avg_pfo = assemble(channel_runner.model.pfo * dx(channel_runner.model.mesh)) / assemble(1.0 * dx(channel_runner.model.mesh))
        err = abs(avg_pfo - target_pfo)
        
        if self.MPI_rank == 0:
          print
          print "Error: " + str(err)
          print
        
        return err
      
      # Do the optimization
      options = {}
      options['maxiter'] = 10
      options['disp'] = True
      res = minimize_scalar(f, bounds=(2e-3, 5e-3), method='bounded', tol = 1.09e-4, options = options)
    
      if MPI_rank == 0:
        print
        print res.x
        
    else :
      ### Non steady state run
      
      channel_runner.run(runner.model.t + T, dt, steady_file = steady_file)
    
     

    

    