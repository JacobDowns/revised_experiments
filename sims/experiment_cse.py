from experiment import *
from sim_constants import *

cse_experiment = Experiment('cse')

spd = sim_constants['spd']

### Trough steady
run1 = cse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-4
run1.run_options['k_bound_high'] = 2e-4
run1.run_options['scale_k_max'] = 7e-4
run1.run_options['end_time'] = 120.0*spd
run1.model_inputs['use_channels'] = True
run1.run_options['tune_atol'] = 1e-8
run1.run_options['dt'] = spd / 64


### Trough winter
run2 = cse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.model_inputs['use_channels'] = True


### Trough winter 1 for basal melt experiment
run3 = cse_experiment.add_run('winter1', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.model_inputs['use_channels'] = True
# 1cm basal melt
run3.run_options['scale_m_min'] = 3.171e-10

  