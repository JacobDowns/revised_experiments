from experiment import *
from sim_constants import *
#from dolfin import *

""" Geometry sensitivity test on Isunnguata Sermia. """

gse_experiment = Experiment('gse')

# Time step for steady state run
spd = sim_constants['spd']
N = 64
dt = spd / N

"""
x0 = -491255.0
y0 = -2.46116e6

#x1 = -491840.0
#y1 = 2.473e6

# Subdomain containing only a single outlet point at terminus
def outlet(x, on_boundary):
  cond1 = abs(x[0] - x0) < 50.0
  cond2 = abs(x[1] - y0) < 50.0
  return cond1 and cond2"""

### Steady state
run1 = gse_experiment.add_run('steady', '../inputs/IS/inputs_is.hdf5', steady = True)
run1.run_options['dt'] = dt
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 3e-3
run1.run_options['k_bound_high'] = 6e-3
run1.run_options['scale_k_max'] = 4e-3
run1.run_options['tune_pfo'] = 0.80
run1.run_options['pvd_interval'] = 1
run1.run_options['pvd_interval'] = N*30
run1.run_options['checkpoint_interval'] = N*30


### Winter
run2 = gse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run2.run_options['constraints'] = True
run2.run_options['scale_k_max'] = run1.run_options['scale_k_max']

### Winter + 3cm basal melt
run3 = gse_experiment.add_run('winter1', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['constraints'] = True
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['scale_m_min'] = 1e-9
