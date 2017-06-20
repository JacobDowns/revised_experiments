from experiment import *

gse_experiment = Experiment('kse')

### Steady state
run1 = gse_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['h_0'] = 0.15
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 4.5e-3
run1.run_options['k_scale_max'] = 5e-3


### Winter
run2 = gse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['h_0'] = 0.15
run2.run_options['constraints'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
  
  