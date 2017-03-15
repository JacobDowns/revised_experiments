from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *

""" 
This script generates steady states fora low, medium, or high
summer sliding velocity on a trough. Conductivity is tuned in each simulation 
to produce a steady state witha spatially averaged pfo of around 0.8 OB. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulation numbers
ns = [1,2,3]

# Name for each run
titles = []
titles.append('steady_trough_l')
titles.append('steady_trough_m')
titles.append('steady_trough_h')

# Input files for each run
input_file = '../../inputs/synthetic/inputs_trough_high.hdf5'

# Velocy scale factors for each run
u_b_scales = [2.0/3.0, 1.0, 4.0/3.0]
# Tuned conductivities for each run
ks = [6e-3, 5.24e-3, 4.9e-3]


for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_file
  model_inputs['out_dir'] = 'results_' + titles[n]
  model_inputs['constants'] = sim_constants
  
  # Create the sheet model
  model = SheetModel(model_inputs)
  
  # Set sliding speed  
  model.u_b.assign(project(model.u_b * Constant(u_b_scales[n]), model.V_cg))
  # Set conductivity
  model.set_k(interpolate(Constant(ks[n]), model.V_cg))
  
  
  ## Run the simulation
  
  # Seconds per day
  spd = pcs['spd']
  # End time
  T = 200.0 * spd
  # Time step
  dt = spd / 3.0
  # Iteration count
  i = 0
  
  while model.t < T:      
    if MPI_rank == 0: 
      current_time = model.t / spd
      print ('Current time: ' + str(current_time))
    
    model.step(dt)

    # Print the average pfo    
    avg_pfo = assemble(model.pfo * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
    
    if MPI_rank == 0: 
      print ("Avg. PFO: ",  avg_pfo)
    
    if i % 3 == 0:
      model.write_pvds(['pfo', 'h'])
      
    if i % 3 == 0:
      model.checkpoint(['h'])
    
    if MPI_rank == 0: 
      print
      
    i += 1
    
  model.write_steady_file('../../inputs/sliding_sensitivity/' + titles[n])