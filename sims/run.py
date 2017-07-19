## Encapsulates a single model run
import sim_constants
from winter_run_opts import *
from steady_run_opts import *
from copy import deepcopy
from dolfin import *

class Run(object):
  def __init__(self, title, input_file, experiment_title = '', steady = True):
    self.title = title
    self.is_steady = steady
    
    if steady :
      self.run_options = deepcopy(steady_run_options)
    else :
      self.run_options = deepcopy(winter_run_options)
    
    model_inputs = {}
    model_inputs['input_file'] = input_file
    model_inputs['out_dir'] = experiment_title + '/' + 'results_' + title
    model_inputs['constants'] = deepcopy(sim_constants)
    model_inputs['steady_file'] = '../inputs/' + experiment_title + '/' + title
    model_inputs['checkpoint_file'] = 'hdf5_results/' + title 
    model_inputs['use_channels'] = False
    # Newton solver parameters
    model_inputs['newton_params'] = NonlinearVariationalSolver.default_parameters()
    model_inputs['newton_params']['newton_solver']['relaxation_parameter'] = 1.0
    model_inputs['newton_params']['newton_solver']['relative_tolerance'] = 1e-12
    model_inputs['newton_params']['newton_solver']['absolute_tolerance'] = 5e-8
    model_inputs['newton_params']['newton_solver']['error_on_nonconvergence'] = False
    model_inputs['newton_params']['newton_solver']['maximum_iterations'] = 30
    
    self.model_inputs = model_inputs
    