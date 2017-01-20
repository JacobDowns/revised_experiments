from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from constants import *
from scale_functions import *

pcs['A'] = 5e-25

# Process number
MPI_rank = MPI.rank(mpi_comm_world())

# Simulations numbers
ns = [3]

# Input files for each run
input_dir = '../../inputs/synthetic/'
input_files = []
input_files.append(input_dir + 'inputs_flat_low.hdf5')
input_files.append(input_dir + 'inputs_flat_high.hdf5')
input_files.append(input_dir + 'inputs_trough_low.hdf5')
input_files.append(input_dir + 'inputs_trough_high.hdf5')

# Name for each run
titles = []
titles.append('steady_flat_low')
titles.append('steady_flat_high')
titles.append('steady_trough_low')
titles.append('steady_trough_high')

# Conductiviities tuned to produce an average steady state pressure of 0.8 OB
ks = [5.2e-3, 5.2e-3, 5.2e-3, 5.24e-3]

for n in ns:
  
  ## Initialize model  
  
  model_inputs = {}
  model_inputs['input_file'] = input_files[n]
  model_inputs['out_dir'] = 'results_' + titles[n]
  model_inputs['constants'] = pcs
  
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
  dt = spd / 8.0
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
    
  model.write_steady_file('../../inputs/steady_sliding_only/' + titles[n])