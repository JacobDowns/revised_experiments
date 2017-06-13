from experiment import *

reference_experiment = Experiment('reference', 're')

### Flat steady
run1 = reference_experiment.add_run('flat_steady', '../inputs/synthetic/inputs_flat_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 3e-2
run1.run_options['k_max'] = 0.00258

### Trough steady
run2 = reference_experiment.add_run('trough_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.run_options['k_bound_low'] = 1e-3
run2.run_options['k_bound_high'] = 3e-2
run2.run_options['k_max'] = 0.00251

### Flat winter
run3 = reference_experiment.add_run('flat_winter', run1.model_inputs['steady_file'], steady = False)

### Trough winter
run4 = reference_experiment.add_run('trough_winter', run2.model_inputs['steady_file'], steady = False)

  
  