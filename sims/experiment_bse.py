from experiment import *

bse_experiment = Experiment('bse')

### 5cm bump height steady
run1 = bse_experiment.add_run('5_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.1
run1.run_options['k_bound_low'] = 3e-3
run1.run_options['k_bound_high'] = 1e-2
run1.run_options['h_0'] = 0.077
run1.run_options['scale_k_max'] = 4.468454086487643612e-03

### 50cm bump height steady
run2 = bse_experiment.add_run('50_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['constants']['h_r'] = 0.5
run2.run_options['k_bound_low'] = 3e-4
run2.run_options['k_bound_high'] = 7e-4
run2.run_options['h_0'] = 0.356
run2.run_options['tune_atol'] = 5e-5
run2.run_options['scale_k_max'] = 5.958462640844880290e-04

### 100cm bump height steady
run3 = bse_experiment.add_run('100_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run3.model_inputs['constants']['h_r'] = 1.0
run3.run_options['k_bound_low'] = 5e-4
run3.run_options['k_bound_high'] = 1e-3
run3.run_options['h_0'] = 0.7
run3.run_options['tune_atol'] = 5e-5
run3.run_options['scale_k_max'] = 0.000244582472001


### 100cm bump height steady
run4 = bse_experiment.add_run('200_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run4.model_inputs['constants']['h_r'] = 2.0
run4.run_options['k_bound_low'] = 8e-5
run4.run_options['k_bound_high'] = 2e-4
run4.run_options['h_0'] = 1.1
run4.run_options['tune_atol'] = 1e-5
run4.run_options['scale_k_max'] = 1.541640786499873846e-04

### 5cm winter
run5 = bse_experiment.add_run('5_winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)

### 50cm winter
run6 = bse_experiment.add_run('50_winter', run2.model_inputs['steady_file'] + '.hdf5', steady = False)

### 100cm winter
run7 = bse_experiment.add_run('100_winter', run3.model_inputs['steady_file'] + '.hdf5', steady = False)

### 200cm winter
run8 = bse_experiment.add_run('200_winter', run4.model_inputs['steady_file'] + '.hdf5', steady = False)
