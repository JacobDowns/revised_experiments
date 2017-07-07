from experiment import *
from sim_constants import *

kge_experiment = Experiment('kge')


spd = sim_constants['spd']
# Day subdivisions
N = 64
# Time step
dt = spd / N

### Steady state
run1 = kge_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['dt'] = dt
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 9e-3
run1.run_options['k_bound_high'] = 1e-2
run1.run_options['scale_k_min'] = 1e-6
run1.run_options['scale_k_max'] = 0.00938196601125
run1.run_options['tune_pfo'] = 0.825
run1.run_options['tune_atol'] = 1e-8
 
### Winter
run2 = kge_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.run_options['constraints'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.run_options['scale_k_lag'] = 0.25 * spd
  
  