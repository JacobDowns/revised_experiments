## Encapsulates a single model run
from experiment_reference import *
from experiment_sliding import *
from experiment_bump import *

experiment_db = {}
experiment_db['reference'] = reference_experiment
experiment_db['sliding'] = sliding_experiment
experiment_db['bump'] = bump_experiment