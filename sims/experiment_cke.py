from experiment import *
from sim_constants import *

cke_experiment = Experiment('cke')
spd = sim_constants['spd']
N = 400

### Trough steady
run1 = cke_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-4
run1.run_options['k_bound_high'] = 2e-4
run1.run_options['scale_k_max'] = 7e-4
run1.run_options['scale_k_min'] = 5e-7
run1.run_options['end_time'] = 120.0*spd
run1.model_inputs['use_channels'] = True
run1.run_options['tune_atol'] = 1e-8
run1.run_options['dt'] = spd / N


### Winter
run2 = cke_experiment.add_run('winter', high_steady, steady = False)
run2.run_options['scale_k'] = True
run2.run_options['vark'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run2.model_inputs['constants']['e_v'] = 1e-4  
run2.model_inputs['use_channels'] = True
run2.run_options['dt'] = spd / N
run2.run_options['pvd_interval'] = N*15
run2.run_options['checkpoint_interval'] = N*2

  