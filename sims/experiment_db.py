## Encapsulates a single model run
from experiment_ref import *
from experiment_sse import *
from experiment_bse import *

experiment_db = {}
experiment_db['ref'] = ref_experiment
experiment_db['sse'] = sse_experiment
experiment_db['bse'] = bse_experiment