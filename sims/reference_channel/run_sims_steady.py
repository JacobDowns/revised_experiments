from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *

""" 
Generates steady states for a flat bed and trough with conductivity tuned to 
produce an average summer PFO of around 0.8 OB.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulation numbers
ns = [1]

# Name for each run
titles = []
titles.append('steady_flat')
titles.append('steady_trough')

# Input files for each run
input_dir = '../../inputs/synthetic/'
input_files = []
input_files.append(input_dir + 'inputs_flat_high.hdf5')
input_files.append(input_dir + 'inputs_trough_high.hdf5')

# Tuned conductivities for each run
ks = [5.2e-3, 5.24e-3]

# Sliding velocity 

for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_files[n]
  model_inputs['out_dir'] = 'results_' + titles[n]
  model_inputs['constants'] = sim_constants
  
  # Create the sheet model
  model = SheetModel(model_inputs)
  
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
    
    if i % 4 == 0:
      model.write_pvds(['pfo', 'h'])
      
    if i % 4 == 0:
      model.checkpoint(['h'])
    
    if MPI_rank == 0: 
      print
      
    i += 1
    
  model.write_steady_file('../../inputs/reference/' + titles[n])