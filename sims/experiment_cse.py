from experiment import *
from sim_constants import *

cse_experiment = Experiment('cse')

### Trough steady
run1 = cse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 4e-3
run1.run_options['scale_k_max'] = 4.487874026589278725e-03
run1.model_inputs['use_channels'] = True


### Trough winter
run2 = cse_experiment.add_run('winter', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run2.model_inputs['use_channels'] = True
  
  