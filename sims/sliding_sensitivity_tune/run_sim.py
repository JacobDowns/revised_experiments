from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *
from sheet_runner import *
import sys

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Summer sliding speed
summer_speed = ['l', 'l', 'm', 'm', 'h', 'h']
# Winter sliding speed
winter_speed = ['h', 'l', 'h', 'l', 'h', 'l']
# Maximum sliding speed for each run
high_max = 100.0
low_max = 5.0
u_b_maxs = [high_max, low_max, high_max, low_max, high_max, low_max]


# Input files for each run
input_file = '../../inputs/sliding_sensitivity_tune/steady_trough_' + summer_speed[n] + '.hdf5'
# Title for each run
title = summer_speed[n] + '_' + winter_speed[n]
# Output directory 
out_dir = 'results_' + title

model_inputs = {}
model_inputs['input_file'] = input_file
model_inputs['out_dir'] = out_dir
model_inputs['constants'] = sim_constants
model_inputs['checkpoint_file'] = title

# Print simulation details
if MPI_rank == 0:
  print "Simulation: " + str(n)
  print "Title: " + title
  print "Input file: " + input_file
  print "Output dir: " + out_dir
  print "Checkpoint file: " + checkpoint_file
  print "u_b_max: " + str(u_b_maxs[n])
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
options['scale_u_b_max'] = u_b_maxs[n]
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']

runner = SheetRunner(model_inputs, options)
runner.run(T, dt)