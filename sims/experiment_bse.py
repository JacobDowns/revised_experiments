from experiment import *

bse_experiment = Experiment('bse')

### 5cm bump height steady
run1 = bse_experiment.add_run('5_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.1
run1.run_options['k_bound_low'] = 3e-3
run1.run_options['k_bound_high'] = 1e-2
run1.run_options['h_0'] = 0.077
r#un1.run_options['scale_k_max'] = 3.769883437553952620e-03

### 50cm bump height steady
run2 = bse_experiment.add_run('50_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['constants']['h_r'] = 0.5
run2.run_options['k_bound_low'] = 4e-4
run2.run_options['k_bound_high'] = 1e-3
run2.run_options['h_0'] = 0.356
run2.run_options['tune_atol'] = 1e-4
#run2.run_options['scale_k_max'] = 4.837694167072586473e-04



### 100cm bump height steady
run3 = bse_experiment.add_run('100_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run3.model_inputs['constants']['h_r'] = 1.0
run3.run_options['k_bound_low'] = 2e-4
run3.run_options['k_bound_high'] = 1e-3
run3.run_options['h_0'] = 0.7
run3.run_options['tune_atol'] = 1e-4
#run3.run_options['scale_k_max'] = 2.021286236252207861e-04

### 100cm bump height steady
run4 = bse_experiment.add_run('200_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run4.model_inputs['constants']['h_r'] = 2.0
run4.run_options['k_bound_low'] = 1e-4
run4.run_options['k_bound_high'] = 1e-3
run4.run_options['h_0'] = 1.25
run4.run_options['tune_atol'] = 1e-4
#run4.run_options['scale_k_max'] = 1.306991867086942851e-04

### 5cm winter
run5 = bse_experiment.add_run('5_winter', run1.model_inputs['steady_file'], steady = False)

### 50cm winter
run6 = bse_experiment.add_run('50_winter', run2.model_inputs['steady_file'], steady = False)

### 100cm winter
run7 = bse_experiment.add_run('100_winter', run3.model_inputs['steady_file'], steady = False)

### 200cm winter
run8 = bse_experiment.add_run('200_winter', run4.model_inputs['steady_file'], steady = False)
