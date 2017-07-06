from experiment import *
from sim_constants import *

cle_experiment = Experiment('cle')
spd = sim_constants['spd']


### Steady state high melt
run1 = cle_experiment.add_run('high_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 9e-5
run1.run_options['k_bound_high'] = 1e-4
run1.run_options['scale_k_max'] = 9.38196601125e-05
run1.run_options['scale_k_min'] = 1e-6
run1.run_options['end_time'] = 1000.0*spd
run1.model_inputs['use_channels'] = True
run1.run_options['tune_atol'] = 1e-8


### Steady state high melt
run2 = cle_experiment.add_run('low_steady', '../inputs/synthetic/inputs_trough_low.hdf5', steady = True)
run2.run_options['vark'] = True
run2.run_options['k_bound_low'] = 2e-4
run2.run_options['k_bound_high'] = 4e-4
run2.run_options['scale_k_max'] = 2.5e-4
run2.run_options['scale_k_min'] = 1e-6
run2.run_options['end_time'] = 1000.0*spd
run2.model_inputs['use_channels'] = True
run2.run_options['tune_atol'] = 1e-8

high_steady = run1.model_inputs['steady_file'] + '.hdf5'
low_steady = run2.model_inputs['steady_file'] + '.hdf5'


### High melt, no lag
run3 = cle_experiment.add_run('high_none', high_steady, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run3.run_options['scale_k_lag'] = 0.0
run3.model_inputs['constants']['e_v'] = 1e-4  
run3.model_inputs['use_channels'] = True


### High melt, one day lag
run4 = cle_experiment.add_run('high_one', high_steady, steady = False)
run4.run_options['scale_k'] = True
run4.run_options['vark'] = True
run4.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run4.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run4.run_options['scale_k_lag'] = spd
run4.model_inputs['constants']['e_v'] = 1e-4  
run4.model_inputs['use_channels'] = True


### High melt, two day lag
run5 = cle_experiment.add_run('high_two', high_steady, steady = False)
run5.run_options['scale_k'] = True
run5.run_options['vark'] = True
run5.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run5.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run5.run_options['scale_k_lag'] = 2.0 * spd
run5.model_inputs['constants']['e_v'] = 1e-4  
run5.model_inputs['use_channels'] = True


### Low melt, no lag
run6 = cle_experiment.add_run('low_none', low_steady, steady = False)
run6.run_options['scale_k'] = True
run6.run_options['vark'] = True
run6.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run6.run_options['scale_k_min'] = run2.run_options['scale_k_min']
run6.run_options['scale_k_lag'] = 0.0
run6.model_inputs['constants']['e_v'] = 1e-4  
run6.model_inputs['use_channels'] = True


### Low melt, one day lag
run7 = cle_experiment.add_run('low_one', low_steady, steady = False)
run7.run_options['scale_k'] = True
run7.run_options['vark'] = True
run7.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run7.run_options['scale_k_min'] = run2.run_options['scale_k_min']
run7.run_options['scale_k_lag'] = spd
run7.model_inputs['constants']['e_v'] = 1e-4 
run7.model_inputs['use_channels'] = True 


### Low melt, two day lag
run8 = cle_experiment.add_run('low_two', low_steady, steady = False)
run8.run_options['scale_k'] = True
run8.run_options['vark'] = True
run8.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run8.run_options['scale_k_min'] = run2.run_options['scale_k_min']
run8.run_options['scale_k_lag'] = 2.0 * spd
run8.model_inputs['constants']['e_v'] = 1e-4 
run8.model_inputs['use_channels'] = True 

  