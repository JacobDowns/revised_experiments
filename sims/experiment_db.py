from experiment_ref import *
from experiment_sse import *
from experiment_bse import *
from experiment_vrse import *
from experiment_kse import *
from experiment_gse import *
from experiment_le import *

experiment_db = {}
experiment_db['ref'] = ref_experiment
experiment_db['sse'] = sse_experiment
experiment_db['bse'] = bse_experiment
experiment_db['vrse'] = vrse_experiment
experiment_db['kse'] = kse_experiment
experiment_db['gse'] = gse_experiment
experiment_db['le'] = le_experiment