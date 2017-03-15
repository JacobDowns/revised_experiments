from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from constants import *
from scale_functions import *

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulations numbers
ns = [0, 1]

# Input files for each run
inputs_flat = '../../inputs/reference/steady_flat.hdf5'
inputs_trough = '../../inputs/reference/steady_trough.hdf5'
input_files = [inputs_flat, inputs_trough]

# Titles for each run
titles = ['flat', 'trough']

for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_files[n]
  model_inputs['out_dir'] = 'results_' + titles[n]
  model_inputs['constants'] = pcs
  
  # Create the sheet model
  model = SheetModel(model_inputs)
  # Object used to get sliding speed and melt input over time
  scale_functions = ScaleFunctions(model.m, model.u_b, u_b_max = 100.0)
  
  
  ## Run the simulation
  
  # Seconds per month
  spm = pcs['spm']
  # Seconds per day
  spd = pcs['spd']
  # End time
  T = 9.0 * spm
  # Time step
  dt = spd / 10.0
  # Iteration count
  i = 0
  
  while model.t < T:  
    # Update the melt
    model.set_m(scale_functions.get_m(model.t))
    # Update the sliding speed
    model.set_u_b(scale_functions.get_u_b(model.t))  
    
    if MPI_rank == 0: 
      current_time = model.t / spd
      print ('Current time: ' + str(current_time))
    
    model.step(dt)
    
    if i % 10 == 0:
      model.write_pvds(['pfo', 'h', 'm', 'u_b'])
      
    if i % 2.0 == 0:
      model.checkpoint(['m', 'pfo', 'h', 'k', 'u_b'])
    
    if MPI_rank == 0: 
      print
      
    i += 1