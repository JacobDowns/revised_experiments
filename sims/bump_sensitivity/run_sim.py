from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *
from sheet_runner import *
import sys

""" 
This script runs one of five winter simulations. Starting from steady states 
with a variety of different bump heights, sliding speed is decreased during the 
fall to a maximum of 100 (m/a) as  melt shuts off. 
"""
# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Bump heights for each run
h_rs = [0.05, 0.1, 0.5, 1.0, 2.0]
# Input files for each run
input_file = '../../inputs/bump_sensitivity/steady_trough_hr_' + str(h_rs[n]) + '.hdf5'
# Title for each run
title = 'trough_hr_' + str(h_rs[n])
# Output directory 
out_dir = 'results_' + title

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = out_dir
sim_constants['h_r'] = h_rs[n]
model_inputs['constants'] = sim_constants


# Print simulation details
if MPI_rank == 0:
  print "Simulation: " + str(n)
  print "Title: " + title
  print "h_r: " + str(h_rs[n])
  print "Input file: " + input_file
  print "Output dir: " + out_dir
  print
  

### Run options

# Seconds per month
spm = pcs['spm']
# Seconds per day
spd = pcs['spd']
# End time
T = 9.0 * spm
# Day subdivisions
N = 48
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N*10
options['checkpoint_interval'] = N/2
options['scale_m'] = True
options['scale_u_b'] = True
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']
options['constraints'] = True

runner = SheetRunner(model_inputs, options)
runner.run(T, dt)
