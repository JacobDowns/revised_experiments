from experiment import *
from sim_constants import *

"""
Reference experiment with constant conductivity, no channels, and no water
sources.
"""

ref_experiment = Experiment('ref')

### Flat steady
run1 = ref_experiment.add_run('flat_steady', '../inputs/synthetic/inputs_flat_high.hdf5', steady = True)
run1.run_options['k_bound_low'] = 4e-3
run1.run_options['k_bound_high'] = 5e-3
run1.run_options['scale_k_max'] = 4.416407864998738234e-03


### Trough steady
run2 = ref_experiment.add_run('trough_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run2.run_options['k_bound_low'] = 3e-3
run2.run_options['k_bound_high'] = 6e-3
run2.run_options['scale_k_max'] = 4.487874026589278725e-03


### Flat winter
run3 = ref_experiment.add_run('flat_winter', run1.model_inputs['steady_file'] + '.hdf5', steady = False)
run3.run_options['scale_k_max'] = run1.run_options['scale_k_max']


### Trough winter
run4 = ref_experiment.add_run('trough_winter', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run4.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run4.run_options['scale_m_min'] = 1e-9


### Trough winter + 3cm basal melt
run5 = ref_experiment.add_run('trough_winter1', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run5.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run5.run_options['scale_m_min'] = 1e-9


### Trough winter + 3cm basal melt + englacial storage
run6 = ref_experiment.add_run('trough_winter2', run2.model_inputs['steady_file'] + '.hdf5', steady = False)
run6.run_options['scale_k_max'] = run2.run_options['scale_k_max']
run6.run_options['scale_m_min'] = 1e-9
run6.model_inputs['constants']['e_v'] = 1e-3
