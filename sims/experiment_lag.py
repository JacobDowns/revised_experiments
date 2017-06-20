from experiment import *
from sim_constants import *
from experiment_kse import *

le_experiment = Experiment('le')
spd = sim_constants['spd']

### Steady state high melt
run1 = kse_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_high.hdf5', steady = True)
run1.run_options['vark'] = True
run1.run_options['k_scale_max'] = experiment_kse.steady_runs['steady'].run_options['scale_k_max']


### Steady state low melt (Don't tune)
run2 = le_experiment.add_run('steady', '../inputs/synthetic/inputs_trough_low.hdf5', steady = True)
run2.run_options['vark'] = True
run2.run_options['k_scale_max'] = experiment_kse.steady_runs['steady'].run_options['scale_k_max']

### High melt, day lag
run1 = lag_experiment.add_run('high_one', steady_file, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = 5e-3
run3.run_options['scale_k_lag'] = spd
run3.model_inputs['constants']['e_v'] = 1e-6


### Winter day lag
run3 = lag_experiment.add_run('one_winter', steady_file, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = 5e-3
run3.run_options['scale_k_lag'] = spd
run3.model_inputs['constants']['e_v'] = 1e-6

### Winter two day lag
run4 = lag_experiment.add_run('day_winter', steady_file, steady = False)
run4.run_options['scale_k'] = True
run4.run_options['vark'] = True
run4.run_options['scale_k_max'] = 5e-3
run4.run_options['scale_k_lag'] = 2.0 * spd
run4.model_inputs['constants']['e_v'] = 1e-6

### Winter week lag
run3 = lag_experiment.add_run('week_winter', steady_file, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = 5e-3
run3.run_options['scale_k_lag'] = 2.0 * spd
run3.model_inputs['constants']['e_v'] = 1e-6
  