from experiment import *

reference_experiment = Experiment('sliding', 'se')

### Slow summer steady
run1 = reference_experiment.add_run('fast_steady', '../inputs/synthetic/inputs_slow_sliding.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 3e-2
run1.run_options['k_max'] = 0.00258

### Noderate summer steady
run2 = reference_experiment.add_run('moderate_steady', '../inputs/synthetic/inputs_moderate_sliding.hdf5', steady = True)
run2.run_options['k_bound_low'] = 1e-3
run2.run_options['k_bound_high'] = 3e-2
run2.run_options['k_max'] = 0.00251

### Noderate summer steady
run3 = reference_experiment.add_run('fast_steady', '../inputs/synthetic/inputs_fast_sliding.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 3e-2
run3.run_options['k_max'] = 0.00251

###  Slow to fast
run5 = reference_experiment.add_run('s_f', run1.model_inputs['steady_file'], steady = False)
run5.run_options['u_b_max'] = 100.0

### Slow to slow
run6 = reference_experiment.add_run('s_s', run1.model_inputs['steady_file'], steady = False)
run6.run_options['u_b_max'] = 5.0

###  Moderate to fast
run7 = reference_experiment.add_run('m_f', run2.model_inputs['steady_file'], steady = False)
run7.run_options['u_b_max'] = 100.0

### Moderate to slow
run8 = reference_experiment.add_run('m_s', run2.model_inputs['steady_file'], steady = False)
run8.run_options['u_b_max'] = 5.0
  
###  Fast to fast
run9 = reference_experiment.add_run('f_f', run3.model_inputs['steady_file'], steady = False)
run9.run_options['u_b_max'] = 100.0

### Fast to slow
run10 = reference_experiment.add_run('f_s', run3.model_inputs['steady_file'], steady = False)
run10.run_options['u_b_max'] = 5.0