from experiment import *
from sim_constants import *

ref_experiment = Experiment('ref')

### Flat steady
run1 = ref_experiment.add_run('flat_steady', '../inputs/synthetic/inputs_flat_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 3e-3
run1.run_options['k_bound_high'] = 6e-3
run1.run_options['scale_k_max'] = 4.416407864998738234e-03

### Trough steady
run2 = ref_experiment.add_run('trough_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.run_options['k_bound_low'] = 3e-3
run2.run_options['k_bound_high'] = 6e-3
run2.run_options['scale_k_max'] = 4.487874026589278725e-03


# Time step
spd = sim_constants['spd']
N = 150
dt = spd / N

### Flat winter
run3 = ref_experiment.add_run('flat_winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['dt'] = dt
run3.run_options['pvd_interval'] = N*15
run3.run_options['checkpoint_interval'] = N*2

### Trough winter
run4 = ref_experiment.add_run('trough_winter', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run4.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run4.run_options['dt'] = dt
run4.run_options['pvd_interval'] = N*15
run4.run_options['checkpoint_interval'] = N*2
  
  