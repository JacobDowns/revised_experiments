from experiment import *

kse_experiment = Experiment('kse')

### Steady state
run1 = kse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 8e-3
run1.run_options['k_scale_max'] = 0.00458806211204

### Winter
run2 = kse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
  
  