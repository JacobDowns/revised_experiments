from experiment import *
from sim_constants import *

cke_experiment = Experiment('cke')
spd = sim_constants['spd']
N = 400

### Trough steady
run1 = cke_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['scale_k_max'] = 9e-4
run1.run_options['scale_k_min'] = 1e-6
run1.run_options['end_time'] = 120.0*spd
run1.model_inputs['use_channels'] = True
run1.run_options['dt'] = spd / N
run1.model_inputs['constants']['e_v'] = 1e-4
run1.run_options['h_0'] = 0.01

### Winter
run2 = cke_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['scale_k'] = True
run2.run_options['vark'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run2.model_inputs['constants']['e_v'] = 1e-4  
run2.model_inputs['use_channels'] = True
run2.run_options['dt'] = spd / N
run2.run_options['pvd_interval'] = N*15
run2.run_options['checkpoint_interval'] = N*2

  