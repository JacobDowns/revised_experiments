from experiment import *
from sim_constants import *

gse_experiment = Experiment('gse')

spd = sim_constants['spd']
# Day subdivisions
N = 24
# Time step
dt = spd / N

### Steady state
run1 = gse_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.model_inputs['constants']['h_r'] = 0.1
run1.run_options['dt'] = dt
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 5e-3
run1.run_options['scale_k_max'] = 0.00183951216287

### Winter
run2 = gse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.model_inputs['constants']['h_r'] = 0.1
run2.run_options['constraints'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
  
  