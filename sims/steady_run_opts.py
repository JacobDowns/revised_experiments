from sim_constants import *

### Default run options for a steady state simulation
steady_run_options = {}

# Run time
spd = sim_constants['spd']
steady_run_options['end_time'] = 200.0 * spd
# Time step
N = 4
dt = spd / N
steady_run_options['dt'] = dt
# Number of iterations between pvd writes
steady_run_options['pvd_interval'] = N*100
# Number of iterations between checkpoint file writes
steady_run_options['checkpoint_interval'] = N*100
# Variables to checkpoints
steady_run_options['checkpoint_vars'] = ['h', 'phi']
# Variables to write to pvds
steady_run_options['pvd_vars'] = ['pfo', 'h']
# Use a spatially variable conductivity?
steady_run_options['vark'] = False
# Min and max conductivity parameters
steady_run_options['scale_k_min'] = 9e-7
steady_run_options['scale_k_max'] = sim_constants['k']
# Bounds on conductivity used for automatic tuning
steady_run_options['k_bound_low'] = 1e-3
steady_run_options['k_bound_high'] = 1e-2
# m_max for melt scaling
steady_run_options['scale_m_max'] = 5.0
# m_min for melt scaling
steady_run_options['scale_m_min'] = 0.0
# Enforce pressure constraints ?
steady_run_options['constraints'] = False
# Target spatially averaged pressure
steady_run_options['tune_pfo'] = 0.85
# Tolerance parameter for tuning
steady_run_options['tune_atol'] = 1.2e-4

