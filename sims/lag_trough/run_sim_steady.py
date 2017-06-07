from dolfin import *
from dolfin import MPI, mpi_comm_world
from sim_constants import *
from sheet_runner import *
import sys
from scipy.optimize import minimize_scalar

""" 
Generates steady states for a trough bed with spatially variable k for lag experiment.
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())


### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['steady_high', 'steady_low']
title = titles[n]

# Input files for each run
input_files = []
input_files.append('../../inputs/synthetic/inputs_trough_high.hdf5')
input_files.append('../../inputs/synthetic/inputs_trough_low.hdf5')
input_file = input_files[n]

# Tuned conductivities for each run
k_max = 0.00709
k_min = 1e-6
m_max = 5.0

# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/lag/' + title

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
  print
  

### Run options

# Seconds per day
spd = pcs['spd']
# End time
T = 250.0 * spd
# Day subdivisions
N = 3
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N*10
options['checkpoint_interval'] = N*10
options['checkpoint_vars'] = ['h']
options['pvd_vars'] = ['pfo', 'h']
options['scale_k_min'] = k_min
options['scale_k_max'] = k_max
options['scale_m_max'] = m_max

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

 # Run simulation
    
runner = SheetRunner(model_inputs, options, pre_step = pre_step)
runner.model.set_k(runner.scale_functions.get_k(0.0))
runner.run(runner.model.t + T, dt, steady_file = steady_file)

"""
### To tune k, we'll use the simplex method

target_pfo = 0.80

# Objective function   
def f(k_max):
  if MPI_rank == 0:
    print "k_max: "  + str(k_max)
    print
  
  runner.scale_functions.k_max = k_max
 
  
  
  # Return average pressure
  avg_pfo = assemble(runner.model.pfo * dx(runner.model.mesh)) / assemble(1.0 * dx(runner.model.mesh))
  err = abs(avg_pfo - target_pfo)
  
  if MPI_rank == 0:
    print
    print "Error: " + str(err)
    print
  
  return err
  
# Do the optimization
options = {}
options['maxiter'] = 10
options['disp'] = True
res = minimize_scalar(f, bounds=(4e-3, 9e-3), method='bounded', tol = 1e-3, options = options)

if MPI_rank == 0:
  print
  print res.x"""