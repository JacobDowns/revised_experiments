from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *

""" 
This script generates steady state for Isunnguata Sermia with spatially variable
k. Target spatially averaged PFO is 0.8.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

# Input file
input_file = '../../inputs/IS/inputs_is.hdf5'
# Tuned conductivities
k_min = 5e-6
k_max = 7e-3
# Title for each run
title = 'steady_is_vark'
# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/realistic_vark/steady_is_vark'

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = out_dir
model_inputs['constants'] = sim_constants

# Print simulation details
if MPI_rank == 0:
  print "Title: " + title
  print "Input file: " + input_file
  print "Output dir: " + out_dir
  print "k_min: " + str(k_min)
  print "k_max: " + str(k_max)
  print
  

### Run options

# Seconds per day
spd = pcs['spd']
# End time
T = 200.0 * spd
# Day subdivisions
N = 24
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N*10
options['checkpoint_interval'] = N*10
options['checkpoint_vars'] = ['h']
options['pvd_vars'] = ['pfo', 'h']
options['scale_k_min'] = k_min
options['scale_k_max'] = k_max
options['constraints'] = True

# Function called prior to each step
def pre_step(model):
  # Print the average pfo    
  avg_pfo = assemble(model.pfo * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
  # Print average water height
  avg_h = assemble(model.h * dx(model.mesh)) / assemble(1.0 * dx(model.mesh))
  
  if MPI_rank == 0:
    print "Avg. PFO: " + str(avg_pfo)
    print "Avg. h: " + str(avg_h)
    print

runner = SheetRunner(model_inputs, options, pre_step = pre_step)
# Set a spatially varying k
runner.model.set_k(runner.scale_functions.get_k(0.0))


### Run simulation

runner.run(T, dt, steady_file = steady_file)
