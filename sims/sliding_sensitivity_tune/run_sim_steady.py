
from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from sheet_runner import *
import sys

""" 
This script generates steady states for various bump heights on a trough geometry.
Conductivity tuned to produce summer steady state pressure around 0.95 OB. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Velocity scale factors for each run
u_b_scales = [2.0/3.0, 1.0, 4.0/3.0]
u_b_scale = ub_scales[n]
# Low, medium, high melt
ms = ['l', 'm', 'h']
# Tuned conductivity for each run
ks = [6e-3, 5.24e-3, 4.9e-3]
k = ks[n]

# Input files for each run
input_file = '../../inputs/synthetic/inputs_trough_high.hdf5'
# Title for each run
title = 'steady_trough' + ms[n]
# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/sliding_sensitivity_tune/' + title

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
  print "u_b scale: " + u_b_scale
  print "k: " + k
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
options['pvd_interval'] = N*10
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
 # Set sliding speed  
runner.model.u_b.assign(project(runner.model.u_b * Constant(u_b_scale), runner.model.V_cg))
# Set conductivity
runner.model.set_k(interpolate(Constant(k),runner.model.V_cg))


### Run simulation

runner.run(T, dt, steady_file = steady_file)