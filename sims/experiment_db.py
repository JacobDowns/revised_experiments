from experiment_ref import *
from experiment_sse import *
from experiment_bse import *
from experiment_vrse import *
from experiment_kse import *
from experiment_gse import *
from experiment_le import *
from experiment_kge import *
from experiment_cse import *
from experiment_cle import *
from experiment_kvar import *

experiment_db = {}
experiment_db['ref'] = ref_experiment
experiment_db['sse'] = sse_experiment
experiment_db['bse'] = bse_experiment
experiment_db['vrse'] = vrse_experiment
experiment_db['kse'] = kse_experiment
experiment_db['gse'] = gse_experiment
experiment_db['le'] = le_experiment
experiment_db['kge'] = kge_experiment
experiment_db['cse'] = cse_experiment
experiment_db['cle'] = cle_experiment
experiment_db['kvar'] = kvar_experiment