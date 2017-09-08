from experiment import *
from sim_constants import *

vkrg_experiment = Experiment('vkrg')

"""
Experiment with variable conductivity, realistic geometry, and some englacial
storage.
"""

# Time step for steady state run
spd = sim_constants['spd']
N = 100
dt = spd / N

### Steady state
run1 = vkrg_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['dt'] = dt
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 9e-3
run1.run_options['k_bound_high'] = 1e-2
run1.run_options['scale_k_min'] = 5e-6
run1.run_options['scale_k_max'] = 5.5e-3
run1.run_options['tune_pfo'] = 0.80
run1.run_options['tune_atol'] = 5e-2
run1.run_options['pvd_interval'] = N*30
run1.run_options['checkpoint_interval'] = N*30
run1.run_options['scale_m_max'] = 2.88746385458


### Winter
run2 = vkrg_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['vark'] = True
run2.run_options['constraints'] = True
run2.run_options['scale_k'] = True
run2.run_options['scale_k_min'] = run1.run_options['scale_k_min']
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run2.model_inputs['constants']['e_v'] = 1e-4
run2.run_options['scale_m_max'] = 2.88746385458
