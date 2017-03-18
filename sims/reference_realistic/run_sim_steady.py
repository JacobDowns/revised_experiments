from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *

""" 
This script generates steady state for Isunnguata Sermia with a target spatially
averaged pressure of 0.8 OB.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

# Input file
input_file = '../../inputs/IS/inputs_is.hdf5'
# Tuned conductivity
k = 5e-3
# Title for each run
title = 'is_steady'
# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/reference_realistic/is_steady'

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = out_dir
model_inputs['constants'] = sim_constants

# Print simulation details
if MPI_rank == 0:
  print "Title: " + title
  print "Input file: " + input_file
  print "Output dir: " + out_dir
  print "k: " + str(k)
  print
  

### Run options

# Seconds per month
spm = pcs['spm']
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
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']
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
# Set conductivity
runner.model.set_k(interpolate(Constant(k),runner.model.V_cg))
# Set a better-ish init. cond.
runner.model.phi.assign(runner.model.phi_0)


### Run simulation

runner.run(T, dt, steady_file = steady_file)
