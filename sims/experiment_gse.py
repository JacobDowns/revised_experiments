from experiment import *
from sim_constants import *

""" Geometry sensitivity test on Isunnguata Sermia. """

gse_experiment = Experiment('gse')

# Time step for steady state run
spd = sim_constants['spd']
N = 64
dt = spd / N

### Steady state
run1 = gse_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['dt'] = dt
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 3e-3
run1.run_options['k_bound_high'] = 6e-3
run1.run_options['scale_k_max'] = 0.0037082039325
run1.run_options['tune_pfo'] = 0.825

### Winter
run2 = gse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['constraints'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']

### Winter + 3cm basal melt
run3 = gse_experiment.add_run('winter1', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['constraints'] = True
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['scale_m_min'] = 1e-9
