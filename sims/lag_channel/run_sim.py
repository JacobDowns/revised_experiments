from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from channel_runner import *
import sys

""" 
Winter simulation on a trough with spatially varying k and high melt input. 
Lag time varies from a day to a week.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['high_day', 'high_week', 'high_month', 'low_day', 'low_week', 'low_month']
title = titles[n]
spd = sim_constants['spd']
lag_times = [spd, 7.*spd, 30.*spd, spd, 7.*spd, 30.*spd]
lag_time = lag_times[n]

# Input files for each run
input_files = []
input_files.append('../../inputs/lag_channel/steady_high.hdf5')
input_files.append('../../inputs/lag_channel/steady_low.hdf5')
input_file = input_files[n / 3]

# Min and max conductivities
k_min = 1e-6
k_max = 3e-3
m_max = 5.0

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
  print "k_min: " + str(k_min)
  print "k_max: " + str(k_max)
  print "m_max: " + str(m_max)
  print "lag: " + str(lag_time / spd)
  print
  

### Run options

# Seconds per month
spm = pcs['spm']
# Seconds per day
spd = pcs['spd']
# End time
T = 9.0 * spm
# Day subdivisions
N = 96
# Time step
dt = spd / N


options = {}
options['pvd_interval'] = N
options['checkpoint_interval'] = N/2
options['scale_m'] = True
options['scale_u_b'] = True
options['scale_k'] = True
options['scale_k_min'] = k_min
options['scale_k_max'] = k_max
options['scale_m_max'] = m_max
options['scale_lag_time'] = lag_time
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']

runner = ChannelRunner(model_inputs, options)
runner.run(T, dt)