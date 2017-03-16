from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *
from sheet_runner import *
import sys

""" 
This script generates steady states for various bump heights on a trough geometry.
Conductivity tuned to produce summer steady state pressure around 0.8 OB. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Initial conditions for each run
hs = [0.025, 0.05, 0.41, 0.6, 1.5]
# Bump heights for each run
h_rs = [0.05, 0.1, 0.5, 1.0, 2.0]
# Bump lengths for each run
l_rs = [2.0, 2.0, 2.0, 2.0, 2.0]
# Tuned conductivities for each run
ks = [1.27e-2, 5.2e-3, 7.1e-4, 3e-4, 1.3e-4]
# Input files for each run
input_file = '../../inputs/synthetic/inputs_trough_high.hdf5'
# Title for each run
title = 'steady_trough_hr_' + str(h_rs[n])
# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/bump_sensitivity/' + title

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = out_dir
model_inputs['constants'] = sim_constants
sim_constants['h_r'] = h_rs[n]
sim_constants['l_r'] = l_rs[n]
model_inputs['constants'] = sim_constants

# Print simulation details
if MPI_rank == 0:
  print "Simulation: " + str(n)
  print "Title: " + title
  print "h_r: " + str(h_rs[n])
  print "k: " + str(ks[n])
  print "Input file: " + input_file
  print "Output dir: " + out_dir
  print
  

### Run options

# Seconds per day
spd = pcs['spd']
# End time
T = 400.0 * spd
# Day subdivisions
N = 3
# Time step
dt = spd / N

options = {}
options['checkpoint_interval'] = N*10
options['checkpoint_interval'] = N*10
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
runner.model.set_k(interpolate(Constant(ks[n]), runner.model.V_cg))
# Set the initial sheet height
runner.model.set_h(interpolate(Constant(hs[n]), runner.model.V_cg))


### Run simulation

runner.run(T, dt, steady_file = steady_file)
