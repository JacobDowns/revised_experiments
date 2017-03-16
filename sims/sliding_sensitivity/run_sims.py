from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *

""" 
This script runs six winter simulations. Starting from steady states with a low,
medium, or high sliding velocity, sliding speed is decreased during the fall to 
either a fast (100 m/a max) or slow (5 m/a max) winter sliding speed. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulations numbers
ns = [5]

# Input files for each run
inputs_l = '../../inputs/sliding_sensitivity/steady_trough_l.hdf5'
inputs_m = '../../inputs/sliding_sensitivity/steady_trough_m.hdf5'
inputs_h = '../../inputs/sliding_sensitivity/steady_trough_h.hdf5'
input_files = []
input_files.append(inputs_l)
input_files.append(inputs_l)
input_files.append(inputs_m)
input_files.append(inputs_m)
input_files.append(inputs_h)
input_files.append(inputs_h)

# Titles for each run
titles = []
titles.append('l_h')
titles.append('l_l')
titles.append('m_h')
titles.append('m_l')
titles.append('h_h')
titles.append('h_l')

# Maximum sliding speed for each run
high_max = 100.0
low_max = 5.0
u_b_maxs = [high_max, low_max, high_max, low_max, high_max, low_max]


for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_files[n]
  model_inputs['out_dir'] = 'results_' + titles[n]
  model_inputs['constants'] = sim_constants
  
  # Create the sheet model
  model = SheetModel(model_inputs)
  
  # Object used to get sliding speed and melt input over time
  scale_functions = ScaleFunctions(model.m, model.u_b, u_b_max = u_b_maxs[n])
  
  
  ## Run the simulation
  
  # Seconds per month
  spm = pcs['spm']
  # Seconds per day
  spd = pcs['spd']
  # End time
  T = 9.0 * spm
  # Day subdivisions
  N = 48
  # Time step
  dt = spd / N
  # Iteration count
  i = 0
  
  while model.t < T:  
    
    if MPI_rank == 0: 
      current_time = model.t / spd
      print ('Current time: ' + str(current_time))
    
    # Update the melt
    model.set_m(scale_functions.get_m(model.t))
    # Update the sliding speed
    model.set_u_b(scale_functions.get_u_b(model.t))  
    
    if i % (N*5) == 0:
      model.write_pvds(['pfo', 'h', 'm', 'u_b'])
    if i % N/2 == 0:
      model.checkpoint(['m', 'pfo', 'h', 'k', 'u_b', 'q', 'N'])
      
    model.step(dt)
    
    if MPI_rank == 0: 
      print
      
    i += 1