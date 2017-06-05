from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from sheet_runner import *
import sys
from scipy.optimize import minimize_scalar

""" 
Generates steady states for a flat bed or trough with conductivity tuned to 
produce an average summer PFO of around 0.95 OB.
"""
set_log_level(50)
# Process number
MPI_rank = MPI.rank(mpi_comm_world())

### Model inputs 

n = 0
if len(sys.argv) > 1:
  n = int(sys.argv[1])

# Name for each run
titles = ['steady_flat', 'steady_trough']
title = titles[n]
# Tuned conductivities for each run
ks = [0.00258, 0.00251]
k = ks[n]

# Input files for each run
input_files = []
input_files.append('../../inputs/synthetic/inputs_flat_high.hdf5')
input_files.append('../../inputs/synthetic/inputs_trough_high.hdf5')
input_file = input_files[n]


# Output directory 
out_dir = 'results_' + title
# Steady state file
steady_file = '../../inputs/reference_tune/' + title

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
  print "k: " + str(k)
  print
  

### Run options

# Seconds per day
spd = pcs['spd']
# End time
T = 150.0 * spd
# Day subdivisions
N = 4
# Time step
dt = spd / N

options = {}
options['pvd_interval'] = N*50
options['checkpoint_interval'] = N*50
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
    
    
### To tune k, we'll use the simplex method
    
runner = SheetRunner(model_inputs, options, pre_step = pre_step)
target_pfo = 0.95

# Objective function   
def f(k):
  if MPI_rank == 0:
    print "k: "  + str(k)
    print
  
  # Set conductivity
  runner.model.set_k(interpolate(Constant(k),runner.model.V_cg))
  # Run simulation
  runner.run(runner.model.t + T, dt, steady_file = steady_file)
  
  
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
res = minimize_scalar(f, bounds=(2.4e-3, 2.7e-3), method='bounded', tol = 1.1e-4, options = options)

if MPI_rank == 0:
  print
  print res.x

  
  