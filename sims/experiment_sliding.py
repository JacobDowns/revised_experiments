from experiment import *

sliding_experiment = Experiment('sliding', 'se')

### Slow summer steady
run1 = sliding_experiment.add_run('slow_steady', '../inputs/synthetic/inputs_slow_sliding.hdf5', steady = True)
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 8e-3
run1.run_options['k_scale_max'] = 0.003790


### Noderate summer steady
run2 = sliding_experiment.add_run('moderate_steady', '../inputs/synthetic/inputs_moderate_sliding.hdf5', steady = True)
run2.run_options['k_bound_low'] = 1e-3
run2.run_options['k_bound_high'] = 8e-3
run2.run_options['k_scale_max'] = 0.003566


### Noderate summer steady
run3 = sliding_experiment.add_run('fast_steady', '../inputs/synthetic/inputs_fast_sliding.hdf5', steady = True)
run3.run_options['k_bound_low'] = 1e-3
run3.run_options['k_bound_high'] = 8e-3
run3.run_options['k_scale_max'] = 0.003491


###  Slow to fast
run4 = sliding_experiment.add_run('s_f_winter', run1.model_inputs['steady_file'], steady = False)
run4.run_options['u_b_max'] = 100.0
run4.run_options['k_scale_max'] = run1.run_options['k_scale_max']

### Slow to slow
run5 = sliding_experiment.add_run('s_s_winter', run1.model_inputs['steady_file'], steady = False)
run5.run_options['u_b_max'] = 5.0
run5.run_options['k_scale_max'] = run1.run_options['k_scale_max']

###  Moderate to fast
run6 = sliding_experiment.add_run('m_f_winter', run2.model_inputs['steady_file'], steady = False)
run6.run_options['u_b_max'] = 100.0
run6.run_options['k_scale_max'] = run2.run_options['k_scale_max']

### Moderate to slow
run7 = sliding_experiment.add_run('m_s_winter', run2.model_inputs['steady_file'], steady = False)
run7.run_options['u_b_max'] = 5.0
run7.run_options['k_scale_max'] = run2.run_options['k_scale_max']
  
###  Fast to fast
run8 = sliding_experiment.add_run('f_f_winter', run3.model_inputs['steady_file'], steady = False)
run8.run_options['u_b_max'] = 100.0
run8.run_options['k_scale_max'] = run3.run_options['k_scale_max']

### Fast to slow
run9 = sliding_experiment.add_run('f_s_winter', run3.model_inputs['steady_file'], steady = False)
run9.run_options['u_b_max'] = 5.0
run9.run_options['k_scale_max'] = run3.run_options['k_scale_max']