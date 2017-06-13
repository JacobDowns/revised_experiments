from experiment import *
from sim_constants import *
from experiment_conductivity import *

lag_experiment = Experiment('lag', 'le')
spd = sim_constants['spd']

# Get the appropriate steady state file
steady_file = conductivity_experiment.steady_runs['steady'].model_inputs['steady_file'] + '.hdf5'

### Winter day lag
run1 = lag_experiment.add_run('one_winter', steady_file, steady = False)
run1.run_options['scale_k'] = True
run1.run_options['vark'] = True
run1.run_options['scale_k_max'] = 5e-3
run1.run_options['scale_k_lag'] = spd
run1.model_inputs['constants']['e_v'] = 1e-6

### Winter two day lag
run2 = lag_experiment.add_run('day_winter', steady_file, steady = False)
run2.run_options['scale_k'] = True
run2.run_options['vark'] = True
run2.run_options['scale_k_max'] = 5e-3
run2.run_options['scale_k_lag'] = 2.0 * spd
run2.model_inputs['constants']['e_v'] = 1e-6

### Winter week lag
run3 = lag_experiment.add_run('week_winter', steady_file, steady = False)
run3.run_options['scale_k'] = True
run3.run_options['vark'] = True
run3.run_options['scale_k_max'] = 5e-3
run3.run_options['scale_k_lag'] = 2.0 * spd
run3.model_inputs['constants']['e_v'] = 1e-6
  