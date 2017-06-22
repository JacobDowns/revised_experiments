from experiment import *

gse_experiment = Experiment('gse')

### Steady state
run1 = gse_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.15
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 4e-3
run1.run_options['scale_k_max'] = 0.00214589803375


### Winter
run2 = gse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.model_inputs['constants']['h_r'] = 0.15
run2.run_options['constraints'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
  
  