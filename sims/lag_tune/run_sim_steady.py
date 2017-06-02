from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *
import sys

""" 
Generates steady states for a flat bed with spatially variable k for lag experiment.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['steady_high', 'steady_low']
title = titles[n]

# Input files for each run
input_files = []
input_files.append('../../inputs/synthetic/inputs_flat_high.hdf5')
input_files.append('../../inputs/synthetic/inputs_flat_low.hdf5')
input_file = input_files[n]

# Tuned conductivities for each run
k_max = 4.8e-3
k_min = 1e-6
m_max = 5.0

# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/lag_tune/' + title

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = out_dir
model_inputs['constants'] = sim_constants

# Print simulation details
if MPI_rank == 0:
  print "Simulation: " + str(n)
  print "Title: " + title
  print "Input file: " + input_file
  print "Output dir: " + out_dir
  print "k_min: " + str(k_min)
  print "k_max: " + str(k_max)
  print "m_max: " + str(m_max)
  print
  

### Run options

# Seconds per day
spd = pcs['spd']
# End time
T = 250.0 * spd
# Day subdivisions
N = 3
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N*10
options['checkpoint_interval'] = N*10
options['checkpoint_vars'] = ['h']
options['pvd_vars'] = ['pfo', 'h']
options['scale_k_min'] = k_min
options['scale_k_max'] = k_max
options['scale_m_max'] = m_max

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