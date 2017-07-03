from experiment import *
from experiment_ref import *

vrse_experiment = Experiment('vrse')
steady_file = ref_experiment.steady_runs['trough_steady'].model_inputs['steady_file'] + '.hdf5'

### Low void ratio
run1 = vrse_experiment.add_run('l_void_winter', steady_file, steady = False)
run1.model_inputs['constants']['e_v'] = 1e-4
run1.run_options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k', 'h_e']
run1.run_options['pvd_vars'] = ['pfo', 'h', 'h_e']
run1.run_options['scale_k_max'] = ref_experiment.steady_runs['trough_steady'].run_options['scale_k_max']

### Medium void ratio
run2 = vrse_experiment.add_run('m_void_winter', steady_file, steady = False)
run2.model_inputs['constants']['e_v'] = 1e-3
run2.run_options['pvd_vars'] = ['pfo', 'h', 'h_e']
run2.run_options['scale_k_max'] = ref_experiment.steady_runs['trough_steady'].run_options['scale_k_max']

### High void ratio
run3 = vrse_experiment.add_run('h_void_winter', steady_file, steady = False)
run3.model_inputs['constants']['e_v'] = 1e-2  
run3.run_options['pvd_vars'] = ['pfo', 'h', 'h_e']
run3.run_options['scale_k_max'] = ref_experiment.steady_runs['trough_steady'].run_options['scale_k_max']

### Basal melt
run4 = vrse_experiment.add_run('basal_winter', steady_file, steady = False)
run4.model_inputs['constants']['e_v'] = 1e-4
run4.run_options['checkpoint_vars'] = ['h', 'pfo', 'q', 'u_b', 'm', 'k', 'h_e']
run4.run_options['pvd_vars'] = ['pfo', 'h', 'h_e']
run4.run_options['scale_k_max'] = ref_experiment.steady_runs['trough_steady'].run_options['scale_k_max']
run4.run_options['m_min'] = 1e-9
