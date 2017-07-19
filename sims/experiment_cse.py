from experiment import *
from sim_constants import *
from dolfin import *

cse_experiment = Experiment('cse')
spd = sim_constants['spd']
N = 250

### Trough steady
run1 = cse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-4
run1.run_options['k_bound_high'] = 2e-4
run1.run_options['scale_k_max'] = 7e-4
run1.run_options['end_time'] = 120.0*spd
run1.model_inputs['use_channels'] = True
run1.run_options['tune_atol'] = 1e-8
run1.run_options['dt'] = spd / 64


### Trough steady with englacial storage
run2 = cse_experiment.add_run('steady1', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.run_options['k_bound_low'] = 1e-4
run2.run_options['k_bound_high'] = 2e-4
run2.run_options['scale_k_max'] = 9e-4
run2.run_options['end_time'] = 120.0*spd
run2.model_inputs['use_channels'] = True
run2.run_options['tune_atol'] = 1e-8
run2.run_options['dt'] = spd / 64
run2.model_inputs['constants']['e_v'] = 1e-3
run2.run_options['scale_m_min'] = 3.171e-10


### Trough winter
run3 = cse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.model_inputs['use_channels'] = True
run3.run_options['dt'] = spd / N
run3.run_options['dt'] = spd / N
run3.run_options['pvd_interval'] = N*15
run3.run_options['checkpoint_interval'] = N*2


### Trough winter 1 for basal melt experiment
run4 = cse_experiment.add_run('winter1', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run4.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run4.model_inputs['use_channels'] = True
run4.run_options['dt'] = spd / N
run4.run_options['pvd_interval'] = N*15
run4.run_options['checkpoint_interval'] = N*2
# 1cm basal melt
run4.run_options['scale_m_min'] = 3.171e-10


### Trough winter 2 for basal melt experiment
run5 = cse_experiment.add_run('winter2', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run5.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run5.model_inputs['use_channels'] = True
run5.run_options['dt'] = spd / N
run5.run_options['pvd_interval'] = N*15
run5.run_options['checkpoint_interval'] = N*2
# 1cm basal melt
run5.run_options['scale_m_min'] = 3.171e-10
# Englacial storage
run5.model_inputs['constants']['e_v'] = 1e-3
# Newton params
run5.model_inputs['newton_params']['newton_solver']['relative_tolerance'] = 5e-10
run5.model_inputs['newton_params']['newton_solver']['absolute_tolerance'] = 1.5e-7


  