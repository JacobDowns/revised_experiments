from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from constants import *
from scale_functions import *

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulations numbers
ns = [0,1,2,3]

# Input files for each run
input_flat = '../../inputs/steady_sliding_only/steady_flat_high.hdf5'
input_trough = '../../inputs/steady_sliding_only/steady_trough_high.hdf5'
input_files = [input_flat, input_flat, input_trough, input_trough]

# Titles for each run
titles = ['flat_fast', 'flat_slow', 'trough_fast', 'trough_slow']

# Maximum sliding speed for each run
u_b_maxs = [100.0, 10.0, 100.0, 10.0]

# Conductiviities used to produce an average steady state pressure of 0.8 OB
k_flat = 5.2e-3
k_trough = 5.24e-3
ks = [k_flat, k_flat, k_trough, k_trough]


for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_files[n]
  model_inputs['out_dir'] = 'results_' + titles[n]
  model_inputs['constants'] = pcs
  
  # Create the sheet model
  model = SheetModel(model_inputs)
  # Object used to get sliding speed and melt input over time
  scale_functions = ScaleFunctions(model.m, model.u_b, u_b_max = u_b_maxs[n])
  # Set conductivity
  model.set_k(interpolate(Constant(ks[n]), model.V_cg))
  
  
  """
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
      print ('%sCurrent time: %s %s' % (fg(1), current_time, attr(0)))
    
    model.step(dt)
    
    if i % 1 == 0:
      model.write_pvds(['pfo', 'h'])
      
    if i % 1 == 0:
      model.checkpoint(['m', 'pfo', 'h', 'u_b', 'k'])
    
    if MPI_rank == 0: 
      print
      
    i += 1"""