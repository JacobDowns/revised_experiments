# -*- coding: utf-8 -*-
"""
Runs the channel model.
"""

from dolfin import *
from dolfin import MPI, mpi_comm_world
from channel_model import *
from scale_functions import *

class ChannelRunner(object):
  
  def __init__(self, run, pre_step = None, post_step = None):
    # Process number
    self.MPI_rank = MPI.rank(mpi_comm_world())
    # Save run object
    self.run = run
    # Create the sheet model
    self.model = ChannelModel(run.model_inputs)
    # Function called before the model is stepped forward each iteration
    self.pre_step = pre_step
    # Function called after the model is stepped forward each iteration
    self.post_step = post_step
    # Seconds per day
    self.spd = 60.0 * 60.0 * 24.0
    # Seconds in a year
    self.spy = 60.0 * 60.0 * 24.0 * 365.0              
    # Seconds per month 
    self.spm = self.spy / 12.0 
        
    ## Scaling object for winter simulation
    self.scale_functions = ScaleFunctions(self.model.m, self.model.u_b, run)    
    
      
  # Runs the sheet model to end time T with time step dt
  def do_run(self, T, dt, steady_file = None):
    
    # Number of iterations
    i = 0
    
    # Run the model to the end time
    while self.model.t < T:      
      
      current_time = self.model.t / self.spd
      self.pprint('Current time: ' + str(current_time))
      
      # Do any desired scalings for winter simulations
      if self.run.run_options['scale_m']:
        self.pprint('Scaling m')
        # Update the melt
        self.model.set_m(self.scale_functions.get_m(self.model.t))
      if self.run.run_options['scale_u_b']:
        self.pprint('Scaling u_b')
        # Update sliding speed
        self.model.set_u_b(self.scale_functions.get_u_b(self.model.t))
      if self.run.run_options['scale_k']:
        self.pprint('Scaling k')
        # Update conductivity
        self.model.set_k(self.scale_functions.get_k(self.model.t))
        
      # Checkpoint and write pvds
      if i % self.run.run_options['checkpoint_interval'] == 0:
        self.model.checkpoint(self.run.run_options['checkpoint_vars'])
      if i % self.run.run_options['pvd_interval'] == 0:
        self.model.write_pvds(self.run.run_options['pvd_vars'])
        
      # Call pre step function
      if self.pre_step:
        self.pre_step(self.model)
      
      # Take a step
      self.model.step(dt, self.run.run_options['constraints'])
      
      # Call post step function
      if self.post_step:
        self.post_step(self.model)
      
      self.pprint('')
      i += 1
      
    # Simulation is file, write steady state file if desired
    if steady_file:
      self.model.write_steady_file(steady_file)
      
    
  # 1 process print
  def pprint(self, s):
    if self.MPI_rank == 0: 
      print s
    


    