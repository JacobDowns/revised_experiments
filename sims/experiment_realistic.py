from experiment import *

realistic_experiment = Experiment('realistic', 're')

### Steady state
run1 = realistic_experiment.add_run('steady', '../../inputs/reference_realistic/is_steady', steady = True)
run1.run_options['constraints'] = True
run1.run_options['k_bound_low'] = 1e-3
run1.run_options['k_bound_high'] = 9e-3

### Winter
run2 = reference_experiment.add_run('winter', run1.model_inputs['steady_file'], steady = False)
run2.run_options['constraints'] = True

  
  