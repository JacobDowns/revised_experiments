from experiment import *
from experiment_kse import *

steady_file = kse_experiment.steady_runs['steady'].model_inputs['steady_file'] + '.hdf5'

kvre_experiment = Experiment('kvre')


### Steady state
run1 = kvre_experiment.add_run('winter1', steady_file, steady = False)
run1.run_options['vark'] = True
run1.run_options['scale_k'] = True
run1.run_options['scale_k_min'] = 1e-6
run1.run_options['scale_k_max'] = kse_experiment.steady_runs['steady'].run_options['scale_k_max']
run1.model_inputs['constants']['e_v'] = 1e-4  


### Steady state
run2 = kvre_experiment.add_run('winter2', steady_file, steady = False)
run2.run_options['vark'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_min'] = 1e-6
run2.run_options['scale_k_max'] = kse_experiment.steady_runs['steady'].run_options['scale_k_max']
run2.model_inputs['constants']['e_v'] = 1e-3