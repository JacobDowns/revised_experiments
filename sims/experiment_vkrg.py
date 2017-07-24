from experiment import *
from sim_constants import *

vkrg_experiment = Experiment('vkrg')


spd = sim_constants['spd']
# Day subdivisions
N = 100
# Time step
dt = spd / N

### Steady state
run1 = vkrg_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['dt'] = dt
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 9e-3
run1.run_options['k_bound_high'] = 1e-2
run1.run_options['scale_k_min'] = 5e-6
run1.run_options['scale_k_max'] = 0.00938196601125
run1.run_options['tune_pfo'] = 0.825
run1.run_options['tune_atol'] = 5e-2
 

### Winter
run2 = vkrg_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.run_options['constraints'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_min'] = run1.run_options['scale_k_min']  
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max'] 
run2.model_inputs['constants']['e_v'] = 1e-4
  