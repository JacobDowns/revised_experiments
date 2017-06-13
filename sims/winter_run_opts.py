from sim_constants import *

# Seconds per month
spm = sim_constants['spm']
# Seconds per day
spd = sim_constants['spd']

### Default run options for a winter simulations
winter_run_options = {}
winter_run_options['end_time'] = 9.0 * spm
# Time step
N = 100
dt = spd / N
winter_run_options['dt'] = dt
# Number of iterations between pvd writes
winter_run_options['pvd_interval'] = N*15
# Number of iterations between checkpoint file writes
winter_run_options['checkpoint_interval'] = N*2
# Variables to checkpoints
winter_run_options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k']
# Variables to write to pvds
winter_run_options['pvd_vars'] = ['pfo', 'h']
# Use a spatially variable conductivity?
winter_run_options['vark'] = False
# Enforce pressure constraints ?
winter_run_options['constraints'] = False
# Scale melt ?
winter_run_options['scale_m'] = True
# m_max for melt scaling
winter_run_options['scale_m_max'] = 5.0
# Scale sliding ?
winter_run_options['scale_u_b'] = True
# Scale conductivity ?
winter_run_options['scale_k'] = False
# Min and max conductivity parameters
winter_run_options['scale_k_min'] = 1e-6
winter_run_options['scale_k_max'] = sim_constants['k']