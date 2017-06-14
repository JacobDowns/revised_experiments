from experiment import *

bump_experiment = Experiment('bump', 'be')

### 5cm bump height steady
run1 = bump_experiment.add_run('5_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.1
run1.run_options['k_bound_low'] = 0.003515 - 1e-6
run1.run_options['k_bound_high'] = 0.003515 + 1e-6
run1.run_options['h_0'] = 0.025
#run1.run_options['k_max'] = 8e-3

### 50cm bump height steady
run2 = bump_experiment.add_run('50_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['constants']['h_r'] = 0.5
run2.run_options['k_bound_low'] = 1e-4
run2.run_options['k_bound_high'] = 1e-3
#run2.run_options['k_max'] = 5e-4

### 100cm bump height steady
run3 = bump_experiment.add_run('100_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run3.model_inputs['constants']['h_r'] = 1.0
run3.run_options['k_bound_low'] = 1e-4
run3.run_options['k_bound_high'] = 1e-3
#run3.run_options['k_max'] = 1e-4

### 100cm bump height steady
run4 = bump_experiment.add_run('200_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run4.model_inputs['constants']['h_r'] = 2.0
run4.run_options['k_bound_low'] = 5e-5
run4.run_options['k_bound_high'] = 5e-4
#run4.run_options['k_max'] = 9e-4

### 5cm winter
run5 = bump_experiment.add_run('5_winter', run1.model_inputs['steady_file'], steady = False)

### 50cm winter
run6 = bump_experiment.add_run('50_winter', run2.model_inputs['steady_file'], steady = False)

### 100cm winter
run7 = bump_experiment.add_run('100_winter', run3.model_inputs['steady_file'], steady = False)

### 200cm winter
run8 = bump_experiment.add_run('200_winter', run4.model_inputs['steady_file'], steady = False)
