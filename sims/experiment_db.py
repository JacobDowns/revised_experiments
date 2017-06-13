## Encapsulates a single model run
from experiment_reference import *
from experiment_sliding import *

experiment_db = {}
experiment_db['reference'] = reference_experiment
experiment_db['sliding'] = sliding_experiment
  
print experiment_db