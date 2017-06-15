from experiment import *

bse_experiment = Experiment('bump', 'bse')

### 5cm bump height steady
run1 = bse_experiment.add_run('5_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.1
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 1e-2
run1.run_options['h_0'] = 0.077
#run2.run_options['scale_k_max'] = 5e-4

### 50cm bump height steady
run2 = bse_experiment.add_run('50_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['constants']['h_r'] = 0.5
run2.run_options['k_bound_low'] = 1e-4
run2.run_options['k_bound_high'] = 1e-3
run2.run_options['h_0'] = 0.356
#run2.run_options['scale_k_max'] = 5e-4

### 100cm bump height steady
run3 = bse_experiment.add_run('100_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run3.model_inputs['constants']['h_r'] = 1.0
run3.run_options['k_bound_low'] = 1e-4
run3.run_options['k_bound_high'] = 8e-4
run3.run_options['h_0'] = 0.7
#run3.run_options['scale_k_max'] = 1e-4

### 100cm bump height steady
run4 = bse_experiment.add_run('200_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run4.model_inputs['constants']['h_r'] = 2.0
run4.run_options['k_bound_low'] = 8e-5
run4.run_options['k_bound_high'] = 3e-4
run3.run_options['h_0'] = 1.25
#run4.run_options['scale_k_max'] = 9e-4

### 5cm winter
run5 = bse_experiment.add_run('5_winter', run1.model_inputs['steady_file'], steady = False)

### 50cm winter
run6 = bse_experiment.add_run('50_winter', run2.model_inputs['steady_file'], steady = False)

### 100cm winter
run7 = bse_experiment.add_run('100_winter', run3.model_inputs['steady_file'], steady = False)

### 200cm winter
run8 = bse_experiment.add_run('200_winter', run4.model_inputs['steady_file'], steady = False)
