from experiment import *
from experiment_reference import *

void_experiment = Experiment('void', 've')

# Get the appropriate steady state file
steady_file = reference_experiment.steady_runs['trough_steady'].model_inputs['steady_file'] + '.hdf5'

### No void winter
run1 = conductivity_experiment.add_run('no_void', steady_file, steady = False)
run1.model_inputs['constants']['e_v'] = 0.0

### Low void winter
run2 = conductivity_experiment.add_run('low_void', steady_file, steady = False)
run2.model_inputs['constants']['e_v'] = 1e-4

### High void winter
run3 = conductivity_experiment.add_run('high_void', steady_file, steady = False)
run3.model_inputs['constants']['e_v'] = 1e-2


  
  