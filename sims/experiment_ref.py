from experiment import *

ref_experiment = Experiment('ref')

### Flat steady
run1 = ref_experiment.add_run('flat_steady', '../inputs/synthetic/inputs_flat_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 3e-3
run1.run_options['k_bound_high'] = 6e-3
run1.run_options['k_scale_max'] = 3.832815729997475929e-03

### Trough steady
run2 = ref_experiment.add_run('trough_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.run_options['k_bound_low'] = 3e-3
run2.run_options['k_bound_high'] = 6e-3
run2.run_options['k_scale_max'] = 3.472135954999579308e-03

### Flat winter
run3 = ref_experiment.add_run('flat_winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['scale_k_max'] = run1.run_options['k_scale_max']

### Trough winter
run4 = ref_experiment.add_run('trough_winter', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run4.run_options['scale_k_max'] = run2.run_options['k_scale_max']
  
  