from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *

""" 
Issunguata Sermia winter simulation with variable k. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

# Input file
input_file = '../../inputs/realistic_vark/steady_is_vark.hdf5'
# Tuned conductivities
k_min = 2e-5
k_max = 7e-3
# Title for each run
title = 'is_vark'
# Output directory 
out_dir = 'results_' + title

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
options['pvd_interval'] = N*5
options['checkpoint_interval'] = N/2
options['scale_m'] = True
options['scale_u_b'] = True
options['scale_k'] = True
options['scale_k_min'] = k_min
options['scale_k_max'] = k_max
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']
options['constraints'] = True



runner = SheetRunner(model_inputs, options)
runner.run(T, dt)
