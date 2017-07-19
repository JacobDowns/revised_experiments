from experiment import *
from sim_constants import *

cke_experiment = Experiment('cke')
spd = sim_constants['spd']


### Steady state high melt
run1 = cke_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 9e-5
run1.run_options['k_bound_high'] = 1e-4
run1.run_options['scale_k_max'] = 9.38196601125e-05
run1.run_options['scale_k_min'] = 5e-7
run1.run_options['end_time'] = 1000.0*spd
run1.model_inputs['use_channels'] = True
run1.run_options['tune_atol'] = 1e-8


### Winter
run3 = cle_experiment.add_run('winter', high_steady, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run3.run_options['scale_k_lag'] = 0.0
run3.model_inputs['constants']['e_v'] = 1e-4  
run3.model_inputs['use_channels'] = True

  