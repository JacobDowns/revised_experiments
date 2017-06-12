from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from sheet_runner import *
import sys

""" 
This script runs one of two reference simulations on a flat bed or trough. 
"""
# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['flat', 'trough']
title = titles[n]
# Input files for each run
input_file = '../../inputs/reference/steady_' + title + '.hdf5'
# Output directory 
out_dir = 'results1_' + title

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
  print
  

### Run options

# Seconds per month
spm = pcs['spm']
# Seconds per day
spd = pcs['spd']
# End time
T = 1.5 * spm
# Day subdivisions
N = 100
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N
options['checkpoint_interval'] = N/2
options['scale_m'] = True
options['scale_u_b'] = True
options['scale_u_b_max'] = 100.0
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
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
runner.model.set_m(project(runner.model.m, runner.model.V_cg))
runner.run(T, dt)
