from experiment import *

void_experiment = Experiment('void', 've')

### Steady state
run1 = conductivity_experiment.add_run('steady', '../inputs/synthetic/inputs_flat_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 8e-3

### Winter
run2 = conductivity_experiment.add_run('winter', run1.model_inputs['steady_file'], steady = False)
run2.run_options['scale_k'] = True
run2.run_options['vark'] = True
run2.run_options['scale_k_max'] = 5e-3

  
  