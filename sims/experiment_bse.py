from experiment import *

bse_experiment = Experiment('bse')

### 5cm bump height steady
run1 = bse_experiment.add_run('5_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.05
run1.run_options['k_bound_low'] = 9e-3
run1.run_options['k_bound_high'] = 5e-2
run1.run_options['h_0'] = 0.025
run1.run_options['scale_k_max'] = 1.041211600369395390e-02

### 50cm bump height steady
run2 = bse_experiment.add_run('50_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['constants']['h_r'] = 0.5
run2.run_options['k_bound_low'] = 3e-4
run2.run_options['k_bound_high'] = 7e-4
run2.run_options['h_0'] = 0.356
run2.run_options['tune_atol'] = 5e-5
run2.run_options['scale_k_max'] = 0.000588051687292

### 100cm bump height steady
run3 = bse_experiment.add_run('100_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run3.model_inputs['constants']['h_r'] = 1.0
run3.run_options['k_bound_low'] = 8e-5
run3.run_options['k_bound_high'] = 3e-4
run3.run_options['h_0'] = 0.7
run3.run_options['tune_atol'] = 1e-7
run3.run_options['scale_k_max'] = 0.00024806504495

### 100cm bump height steady
run4 = bse_experiment.add_run('200_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run4.model_inputs['constants']['h_r'] = 2.0
run4.run_options['k_bound_low'] = 1e-4
run4.run_options['k_bound_high'] = 3e-4
run4.run_options['h_0'] = 1.3
run4.run_options['tune_atol'] = 1e-7
run4.run_options['scale_k_max'] = 9.61803398875e-05

### 5cm winter
run5 = bse_experiment.add_run('5_winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run5.model_inputs['constants']['h_r'] = run1.model_inputs['constants']['h_r']
run5.run_options['scale_k_max'] = run1.run_options['scale_k_max']

### 50cm winter
run6 = bse_experiment.add_run('50_winter', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run6.model_inputs['constants']['h_r'] = run2.model_inputs['constants']['h_r']
run6.run_options['scale_k_max'] = run2.run_options['scale_k_max']

### 100cm winter
run7 = bse_experiment.add_run('100_winter', run3.model_inputs['steady_file'] + '.hdf5', steady = False)
run7.model_inputs['constants']['h_r'] = run3.model_inputs['constants']['h_r']
run7.run_options['scale_k_max'] = run3.run_options['scale_k_max']

### 200cm winter
run8 = bse_experiment.add_run('200_winter', run4.model_inputs['steady_file'] + '.hdf5', steady = False)
run8.model_inputs['constants']['h_r'] = run4.model_inputs['constants']['h_r']
run8.run_options['scale_k_max'] = run4.run_options['scale_k_max']