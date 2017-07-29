from experiment import *
from sim_constants import *
import numpy as np

cse1_experiment = Experiment('cse1')
spd = sim_constants['spd']
N = 200

shutoff_length = 15.0 * spd

def scale_m(t):
  m_s = 1.0
  if t <= shutoff_length:
    m_s = np.sin((np.pi / (2.0 * shutoff_length)) * t)
    
  return m_s

### Summer
# No melt sources
run1 = cse1_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.model_inputs['use_channels'] = True
run1.run_options['end_time'] = 120.0*spd
run1.run_options['scale_k_max'] = 1e-3
run1.run_options['dt'] = spd / N
run1.run_options['scale_m'] = True
run1.run_options['scale_m_scale'] = scale_m
run1.run_options['h_0'] = 0.02


### Summer1
# 1cm basal melt + englacial storage
run2 = cse1_experiment.add_run('steady1', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.model_inputs['use_channels'] = True
run2.run_options['end_time'] = 120.0*spd
run2.run_options['scale_k_max'] = 1e-3
run2.run_options['dt'] = spd / N
run2.run_options['scale_m'] = True
run2.run_options['scale_m_scale'] = scale_m 
run2.model_inputs['constants']['e_v'] = 1e-3
run2.run_options['scale_m_min'] = 3.171e-10
run2.run_options['h_0'] = 0.02


  