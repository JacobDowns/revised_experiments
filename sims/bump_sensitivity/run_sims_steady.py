from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *

""" 
This script generates steady states for various bump heights on a trough geometry.
Conductivity tuned to produce summer steady state pressure around 0.8 OB. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulation numbers
ns = [4]

# Name for each run
titles = []
titles.append('steady_trough_hr_0.05')
titles.append('steady_trough__hr_0.1')
titles.append('steady_trough_hr_0.5')
titles.append('steady_trough_hr_1')
titles.append('steady_trough_hr_2')

# Input files for each run
input_file = '../../inputs/synthetic/inputs_trough_high.hdf5'

# Initial conditions for each run
hs = [0.025, 0.05, 0.41, 0.6, 1.5]
# Bump heights for each run
h_rs = [0.05, 0.1, 0.5, 1.0, 2.0]
# Bump lengths for each run
l_rs = [2.0, 2.0, 2.0, 2.0, 2.0]
# Tuned conductivities for each run
ks = [1.27e-2, 5.2e-3, 7.1e-4, 3e-4, 1.3e-4]


for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_file
  model_inputs['out_dir'] = 'results_' + titles[n]
  
  sim_constants['h_r'] = h_rs[n]
  sim_constants['l_r'] = l_rs[n]
  model_inputs['constants'] = sim_constants

  # Create the sheet model
  model = SheetModel(model_inputs)
  
  # Set conductivity
  model.set_k(interpolate(Constant(ks[n]), model.V_cg))
  # Set the initial sheet height
  model.set_h(interpolate(Constant(hs[n]), model.V_cg))
  
  
  ## Run the simulation
  
  # Seconds per day
  spd = pcs['spd']
  # End time
  T = 450.0 * spd
  # Day subdivisions 
  N = 3
  # Time step
  dt = spd / N
  # Iteration count
  i = 0
  
  while model.t < T:      
    if MPI_rank == 0: 
      current_time = model.t / spd
      print ('Current time: ' + str(current_time))
    
    model.step(dt)

    # Print the average pfo    
    avg_pfo = assemble(model.pfo * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
    # Print average water height
    avg_h = assemble(model.h * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))

    if MPI_rank == 0: 
      print ("Avg. PFO: ",  avg_pfo)
      print ("Avg. h: ", avg_h)
    
    if i % (10*N) == 0:
      model.write_pvds(['pfo', 'h'])
      model.checkpoint(['h'])
    
    if MPI_rank == 0: 
      print
      
    i += 1
    
  model.write_steady_file('../../inputs/sliding_sensitivity/' + titles[n])
