from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *
import sys

""" 
Winter simulation on flat bed with spatially varying k and either high or low
melt input. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['high', 'low']
title = titles[n]

# Input files for each run
input_files = []
input_files.append('../../inputs/synthetic_vark/steady_high.hdf5')
input_files.append('../../inputs/synthetic_vark/steady_low.hdf5')
input_file = input_files[n]

# Tuned conductivities for each run
k_maxs = [7e-3, 3.5e-3]
k_mins = [5e-6, 5e-6]

# Output directory 
out_dir = 'results_' + title

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
  print "k_min: " + str(k_mins[n])
  print "k_max: " + str(k_maxs[n])
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
options['scale_k'] = True
options['scale_k_min'] = k_mins[n]
options['scale_k_max'] = k_maxs[n]
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']

runner = SheetRunner(model_inputs, options)
runner.run(T, dt)