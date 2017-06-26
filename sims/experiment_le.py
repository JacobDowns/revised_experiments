from experiment import *
from sim_constants import *
from experiment_kse import *

le_experiment = Experiment('le')
spd = sim_constants['spd']
scale_k_max = kse_experiment.steady_runs['steady'].run_options['scale_k_max']

### Steady state high melt
run1 = le_experiment.add_run('high_steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['scale_k_max'] = scale_k_max
run1.run_options['scale_m_max'] = 5.0


### Steady state low melt
run2 = le_experiment.add_run('low_steady', '../inputs/synthetic/inputs_trough_low.hdf5', steady = True)
run2.run_options['vark'] = True
run2.run_options['scale_k_max'] = scale_k_max
run2.run_options['scale_m_max'] = 5.0


high_steady = run1.model_inputs['steady_file'] + '.hdf5'
low_steady = run2.model_inputs['steady_file'] + '.hdf5'


### High melt, no lag
run3 = le_experiment.add_run('high_none', high_steady, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = scale_k_max
run3.run_options['scale_k_lag'] = 0.0


### High melt, one day lag
run4 = le_experiment.add_run('high_one', high_steady, steady = False)
run4.run_options['scale_k'] = True
run4.run_options['vark'] = True
run4.run_options['scale_k_max'] = scale_k_max
run4.run_options['scale_k_lag'] = spd


### High melt, two day lag
run5 = le_experiment.add_run('high_two', high_steady, steady = False)
run5.run_options['scale_k'] = True
run5.run_options['vark'] = True
run5.run_options['scale_k_max'] = scale_k_max
run5.run_options['scale_k_lag'] = 2.0 * spd


### Low melt, no lag
run6 = le_experiment.add_run('low_none', low_steady, steady = False)
run6.run_options['scale_k'] = True
run6.run_options['vark'] = True
run6.run_options['scale_k_max'] = scale_k_max
run6.run_options['scale_k_lag'] = 0.0


### Low melt, one day lag
run7 = le_experiment.add_run('low_one', low_steady, steady = False)
run7.run_options['scale_k'] = True
run7.run_options['vark'] = True
run7.run_options['scale_k_max'] = scale_k_max
run7.run_options['scale_k_lag'] = spd


### Low melt, two day lag
run8 = le_experiment.add_run('low_two', low_steady, steady = False)
run8.run_options['scale_k'] = True
run8.run_options['vark'] = True
run8.run_options['scale_k_max'] = scale_k_max
run8.run_options['scale_k_lag'] = 2.0 * spd

  