from experiment import *
from sim_constants import *

kse_experiment = Experiment('kse')
spd = sim_constants['spd']

N = 250
dt = spd / N

### Steady state
run1 = kse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_bound_low'] = 4e-3
run1.run_options['k_bound_high'] = 8e-3
run1.run_options['scale_k_min'] = 4e-8
run1.run_options['scale_k_max'] = 0.005527864045

 

### Winter 1
run2 = kse_experiment.add_run('winter1', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.run_options['dt'] = dt
run2.run_options['pvd_interval'] = N*15
run2.run_options['checkpoint_interval'] = N*2


### Winter 2
run3 = kse_experiment.add_run('winter2', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['vark'] = True
run3.run_options['scale_k'] = True
run3.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['scale_k_lag'] = 0.25 * spd
run3.run_options['dt'] = dt
run3.run_options['pvd_interval'] = N*15
run3.run_options['checkpoint_interval'] = N*2

