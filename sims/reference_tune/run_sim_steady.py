from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from sheet_runner import *
import sys

""" 
Generates steady states for a flat bed or trough with conductivity tuned to 
produce an average summer PFO of around 0.95 OB.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['steady_flat', 'steady_trough']
title = titles[n]
# Tuned conductivities for each run
ks = [2.6e-3, 2.6e-3]
k = ks[n]

# Input files for each run
input_files = []
input_files.append('../../inputs/synthetic/inputs_flat_high.hdf5')
input_files.append('../../inputs/synthetic/inputs_trough_high.hdf5')
input_file = input_files[n]


# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/reference_tune/' + title

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
  print "k: " + str(k)
  print
  

### Run options

# Seconds per day
spd = pcs['spd']
# End time
T = 400.0 * spd
# Day subdivisions
N = 4
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N*50
options['checkpoint_interval'] = N*50
options['checkpoint_vars'] = ['h']
options['pvd_vars'] = ['pfo', 'h']

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
# Set conductivity
runner.model.set_k(interpolate(Constant(k),runner.model.V_cg))


### Run simulation

runner.run(T, dt, steady_file = steady_file)