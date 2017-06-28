from experiment import *
from experiment_kse import *

steady_file = kse_experiment.steady_runs['steady'].model_inputs['steady_file'] + '.hdf5'

kvar_experiment = Experiment('kvar')

"""
### Winter 1
run1 = kvar_experiment.add_run('winter1', steady_file, steady = False)
run1.run_options['vark'] = True
run1.run_options['scale_k'] = True
run1.run_options['scale_k_min'] = 1e-6
run1.run_options['scale_k_max'] = kse_experiment.steady_runs['steady'].run_options['scale_k_max']
run1.model_inputs['constants']['e_v'] = 1e-4  


### Winter 2
run2 = kvar_experiment.add_run('winter2', steady_file, steady = False)
run2.run_options['vark'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_min'] = 1e-6
run2.run_options['scale_k_max'] = kse_experiment.steady_runs['steady'].run_options['scale_k_max']
run2.model_inputs['constants']['e_v'] = 1e-3"""


### Winter 3
run3 = kvar_experiment.add_run('winter3', steady_file, steady = False)
run3.run_options['vark'] = True
run3.run_options['scale_k'] = True
run3.run_options['scale_k_min'] = 1e-5
run3.run_options['scale_k_max'] = kse_experiment.steady_runs['steady'].run_options['scale_k_max']
run3.run_options['scale_m_min'] = 1e-9
run3.model_inputs['constants']['e_v'] = 1e-4  