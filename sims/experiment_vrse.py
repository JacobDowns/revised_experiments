from experiment import *
from experiment_ref import *

vrse_experiment = Experiment('vrse')
steady_file = ref_experiment.steady_runs['trough_steady'].model_inputs['steady_file'] + '.hdf5'

### Low void ratio
run1 = vrse_experiment.add_run('l_void_winter', steady_file, steady = False)
run1.model_inputs['constants']['e_v'] = 1e-4

### Medium void ratio
run2 = vrse_experiment.add_run('m_void_winter', steady_file, steady = False)
run2.model_inputs['constants']['e_v'] = 1e-3

### High void ratio
run3 = vrse_experiment.add_run('h_void_winter', steady_file, steady = False)
run3.model_inputs['constants']['e_v'] = 1e-2  
  