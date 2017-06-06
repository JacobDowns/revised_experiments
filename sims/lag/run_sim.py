from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *
import sys

""" 
Winter simulation on flat bed with spatially varying k and high melt input. 
Lag time varies from a day to a week.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['high_one', 'high_two', 'high_week', 'low_one', 'low_two', 'low_week']
title = titles[n]
spd = sim_constants['spd']
lag_times = [spd, 2.*spd, 7.*spd]
lag_time = lag_times[n % 3]
# I've noted that if there is very little water in the sheet as in the week lag 
# runs, there is some instability that occurs when k is decreased that causes
# slight negative pressures that  begin to corrupt the solution. To avoid this
# we use constraints for this run.
constraints = [False, False, True]
constrain = constraints[n % 3]


# Input files for each run
input_files = []
input_files.append('../../inputs/lag/steady_high.hdf5')
input_files.append('../../inputs/lag/steady_low.hdf5')
input_file = input_files[n / 3]

# Min and max conductivities
k_max = 7e-3
k_min = 1e-6
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
  print "lag: " + str(lag_time / spd)
  print "m_max: " + str(m_max)
  print "constrain: " + str(constrain)
  print  

### Run options

# Seconds per month
spm = pcs['spm']
# Seconds per day
spd = pcs['spd']
# End time
T = 9.0 * spm
# Day subdivisions
N = 300
# Time step
dt = spd / N


options = {}
options['pvd_interval'] = N*30
options['checkpoint_interval'] = N/2
options['scale_m'] = True
options['scale_u_b'] = True
options['scale_k'] = True
options['scale_k_min'] = k_min
options['scale_k_max'] = k_max
options['scale_m_max'] = m_max
options['scale_lag_time'] = lag_time
options['constraints'] = True
options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
options['pvd_vars'] = ['pfo', 'h']

# Function called prior to each step
def pre_step(model):
  min_pfo = model.pfo.vector().min()
  min_h = model.h.vector().min()
  
  if MPI_rank == 0:
    print "Min. PFO: " + str(min_pfo)
    print "Min. h: " + str(min_h)
    print

runner = SheetRunner(model_inputs, options, pre_step = pre_step)
runner.run(T, dt)