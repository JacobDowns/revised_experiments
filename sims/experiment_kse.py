from experiment import *

kse_experiment = Experiment('kse')

### Steady state
run1 = kse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 4e-3
run1.run_options['k_bound_high'] = 8e-3
run1.run_options['scale_k_min'] = 9e-7
run1.run_options['scale_k_max'] = 0.005527864045


### Steady state 1
run2 = kse_experiment.add_run('steady1', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.run_options['vark'] = True
run2.run_options['k_bound_low'] = 4e-3
run2.run_options['k_bound_high'] = 8e-3
run2.run_options['scale_k_min'] = 8e-7
run2.run_options['scale_k_max'] = 0.005527864045


### Steady state 2
run3 = kse_experiment.add_run('steady2', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run3.run_options['vark'] = True
run3.run_options['k_bound_low'] = 4e-3
run3.run_options['k_bound_high'] = 8e-3
run3.run_options['scale_k_min'] = 5e-7
run3.run_options['scale_k_max'] = 0.005527864045


### Winter
run4 = kse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run4.run_options['vark'] = True
run4.run_options['scale_k'] = True
run4.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run4.run_options['scale_k_max'] = run1.run_options['scale_k_max']
 

### Winter 1
run5 = kse_experiment.add_run('winter1', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run5.run_options['vark'] = True
run5.run_options['scale_k'] = True
run5.run_options['scale_k_min'] = run2.run_options['scale_k_min']
run5.run_options['scale_k_max'] = run2.run_options['scale_k_max']


### Winter 2
run6 = kse_experiment.add_run('winter2', run3.model_inputs['steady_file'] + '.hdf5', steady = False)
run6.run_options['vark'] = True
run6.run_options['scale_k'] = True
run6.run_options['scale_k_min'] = run3.run_options['scale_k_min']
run6.run_options['scale_k_max'] = run3.run_options['scale_k_max']