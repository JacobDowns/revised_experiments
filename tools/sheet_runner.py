# -*- coding: utf-8 -*-
"""
Runs the channel model.
"""

from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from scale_functions import *
import pickle

class SheetRunner(object):
  
  def __init__(self, model_inputs, options = None, pre_step = None, post_step = None):
    # Process number
    self.MPI_rank = MPI.rank(mpi_comm_world())
    # Create the sheet model
    self.model = SheetModel(model_inputs)
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
        
    ## Runner options
        
    self.options = {}
    # Number of time steps between pvd writes
    self.options['pvd_interval'] = 1
    # Number of time steps between checkpoints
    self.options['checkpoint_interval'] = 1
    # Checkpoint variables
    self.options['checkpoint_vars'] = ['h', 'q']
    # Variables to write as pvds
    self.options['pvd_vars'] = ['pfo', 'h']
    # Scale m in winter simulation?
    self.options['scale_m'] = False
    # Scale u_b for in winter simulation?
    self.options['scale_u_b'] = False
    # Scale k in winter simulation?
    self.options['scale_k'] = False
    # k_min, and k_max for winter scaling 
    self.options['scale_k_min'] = 5e-5
    self.options['scale_k_max'] = 5e-3
    # m_max for winter conductivity scaling
    self.options['scale_m_max'] = None
    # Duration of melt shut off for winter scaling
    self.options['scale_shutoff_length'] = 30.0 * self.spd
    # Lag of conductivity behind melt for winter simulations
    self.options['scale_lag_time'] = 0.0
    # u_b_max for winter  scaling
    self.options['scale_u_b_max'] = 100.0
    # Turn on pressure constraints
    self.options['constraints'] = False
    
    # Overwrite any changed options
    if options:
      for key in options.keys():
        self.options[key] = options[key]
    
    # Write out the run options 
    pickle.dump(self.options, open(model_inputs['out_dir'] + '/run_config.p', 'wb'))
        
        
    ## Scaling object for winter simulation
    self.scale_functions = ScaleFunctions(self.model.m, self.model.u_b, 
        k_min = self.options['scale_k_min'], 
        k_max = self.options['scale_k_max'], 
        u_b_max = self.options['scale_u_b_max'],
        shutoff_length = self.options['scale_shutoff_length'],
        lag_time = self.options['scale_lag_time'],
        m_max = self.options['scale_m_max'])    
    
      
  # Runs the sheet model to end time T with time step dt
  def run(self, T, dt, steady_file = None):
    
    # Number of iterations
    i = 0
    
    # Run the model to the end time
    while self.model.t < T:      
      
      current_time = self.model.t / self.spd
      self.pprint('Current time: ' + str(current_time))
      
      # Do any desired scalings for winter simulations
      if self.options['scale_m']:
        self.pprint('Scaling m')
        # Update the melt
        self.model.set_m(self.scale_functions.get_m(self.model.t))
      if self.options['scale_u_b']:
        self.pprint('Scaling u_b')
        # Update sliding speed
        self.model.set_u_b(self.scale_functions.get_u_b(self.model.t))
      if self.options['scale_k']:
        self.pprint('Scaling k')
        # Update conductivity
        self.model.set_k(self.scale_functions.get_k(self.model.t))
        
      # Checkpoint and write pvds
      if i % self.options['checkpoint_interval'] == 0:
        self.model.checkpoint(self.options['checkpoint_vars'])
      if i % self.options['pvd_interval'] == 0:
        self.model.write_pvds(self.options['pvd_vars'])
        
      # Call pre step function
      if self.pre_step:
        self.pre_step(self.model)
      
      if self.options['constraints']:
        # Take a step with constraints
        self.model.step_constrained(dt)
      else :
        # Take a step
        self.model.step(dt)
      
      # Call post step function
      if self.post_step:
        self.post_step(self.model)
      
      self.pprint('')
      i += 1
      
    # Simulation is done, write steady state file if desired
    if steady_file:
      self.model.write_steady_file(steady_file)
    
    
  # 1 process print
  def pprint(self, s):
    if self.MPI_rank == 0: 
      print s
    


    