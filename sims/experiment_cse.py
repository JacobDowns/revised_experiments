from experiment import *
from sim_constants import *
import numpy as np

cse_experiment = Experiment('cse')
spd = sim_constants['spd']
N = 400

shutoff_length = 7.0 * spd

def scale_m(t):
  m_s = 1.0
  if t <= shutoff_length:
    m_s = np.sin((np.pi / (2.0 * shutoff_length)) * t)
    
  return m_s

### Summer
# No melt sources
run1 = cse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['use_channels'] = True
run1.run_options['end_time'] = 120.0*spd
run1.run_options['scale_k_max'] = 8e-4
run1.run_options['dt'] = spd / N
run1.run_options['h_0'] = 0.01
run1.run_options['scale_m'] = True
run1.run_options['scale_m_scale'] = scale_m
run1.run_options['h_0'] = 0.01


### Summer1
# 1cm basal melt + englacial storage
run2 = cse_experiment.add_run('steady1', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['use_channels'] = True
run2.run_options['end_time'] = 120.0*spd
run2.run_options['scale_k_max'] = 8e-4
run2.run_options['dt'] = spd / N
run2.run_options['h_0'] = 0.01
run2.run_options['scale_m'] = True
run2.run_options['scale_m_scale'] = scale_m
run2.model_inputs['constants']['e_v'] = 1e-3
run2.run_options['scale_m_min'] = 3.171e-10
run2.run_options['h_0'] = 0.01


### Winter
# No melt sources
run3 = cse_experiment.add_run('winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.model_inputs['use_channels'] = True
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']
run3.run_options['dt'] = spd / N
run3.run_options['pvd_interval'] = N*15
run3.run_options['checkpoint_interval'] = N*2


### Winter1
# 1cm basal melt + englacial storage
run4 = cse_experiment.add_run('winter1', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run4.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run4.model_inputs['use_channels'] = True
run4.run_options['dt'] = spd / N
run4.run_options['pvd_interval'] = N*15
run4.run_options['checkpoint_interval'] = N*2
run4.model_inputs['constants']['e_v'] = 1e-3
run4.run_options['scale_m_min'] = 3.171e-10


  