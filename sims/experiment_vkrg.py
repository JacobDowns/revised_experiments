from experiment import *

vkrg_experiment = Experiment('vkrg')

### Steady state
run1 = vkrg_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['vark'] = True
run1.model_inputs['constants']['h_r'] = 0.15
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 5e-3
run1.run_options['k_bound_high'] = 6.5e-3
run1.run_options['scale_k_max'] = 0.00535410196625


### Winter
run2 = vkrg_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.model_inputs['constants']['h_r'] = 0.15
run2.model_inputs['constants']['e_v'] = 1e-8  
run2.run_options['constraints'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.run_options['scale_k_min'] = 1e-6
  
  