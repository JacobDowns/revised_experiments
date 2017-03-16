from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *

""" 
This script generates steady state for Isunnguata Sermia with a target spatially
averaged pressure of 0.8 OB.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Input files for each run
input_file = '../../inputs/IS/inputs_is.hdf5'
# Tuned conductivity
k = 5e-3

  
## Initialize model  

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = 'results_is_steady' 
model_inputs['constants'] = sim_constants

# Create the sheet model
model = SheetModel(model_inputs)
# Set conductivity
model.set_k(interpolate(Constant(k), model.V_cg))


## Run the simulation

# Seconds per day
spd = pcs['spd']
# End time
T = 200.0 * spd
# Day subdivisions
N = 24
# Time step
dt = spd / N
# Iteration count
i = 0

while model.t < T:      
  if MPI_rank == 0: 
    current_time = model.t / spd
    print ('Current time: ' + str(current_time))
    
  if i % (N*5) == 0:
    model.write_pvds(['pfo', 'h'])
    model.checkpoint(['h'])
  
  model.step_constrained(dt)

  # Print the average pfo    
  avg_pfo = assemble(model.pfo * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
  
  if MPI_rank == 0: 
    print ("Avg. PFO: ",  avg_pfo)
  

  
  if MPI_rank == 0: 
    print
    
  i += 1
  
model.write_steady_file('../../inputs/reference_realistic/is_steady')