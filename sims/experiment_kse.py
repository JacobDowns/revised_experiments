from experiment import *

kse_experiment = Experiment('kse')

### Steady state
run1 = kse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 4e-3
run1.run_options['k_bound_high'] = 8e-3
run1.run_options['scale_k_max'] = 0.005527864045


print run1.model_inputs['steady_file'] + '.hdf5'

quit()

### Winter
run2 = kse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']


### Winter with a small storage term
run3 = kse_experiment.add_run('winter1', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['vark'] = True
run3.run_options['scale_k'] = True
run3.run_options['scale_k_min'] = 1e-6
run3.model_inputs['constants']['e_v'] = 1e-6  
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']