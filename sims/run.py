import sim_constants
from winter_run_opts import *
from steady_run_opts import *
from copy import deepcopy
from dolfin import NonlinearVariationalSolver

"""
Object representing a single model run. Specifies lots of default options that
can be overwritten.
"""

class Run(object):
  def __init__(self, title, input_file, experiment_title = '', steady = True):
    self.title = title
    self.is_steady = steady

    # Default options
    self.run_options = {}
    # Number of time steps between pvd writes
    self.run_options['pvd_interval'] = 1
    # Number of time steps between checkpoints
    self.run_options['checkpoint_interval'] = 1
    # Checkpoint variables
    self.run_options['checkpoint_vars'] = ['h', 'q', 'S', 'phi']
    # Variables to write as pvds
    self.run_options['pvd_vars'] = ['pfo', 'h']
    # Scale m in winter simulation?
    self.run_options['scale_m'] = False
    # Scale u_b for in winter simulation?
    self.run_options['scale_u_b'] = False
    # Scale k in winter simulation?
    self.run_options['scale_k'] = False
    # k_min, and k_max for winter scaling
    self.run_options['scale_k_min'] = 5e-5
    self.run_options['scale_k_max'] = 5e-3
    # m_max for winter conductivity scaling
    self.run_options['scale_m_max'] = None
    # Duration of melt shut off for winter scaling
    self.run_options['scale_shutoff_length'] = 30.0 * sim_constants['spd']
    # Lag of conductivity behind melt for winter simulations
    self.run_options['scale_k_lag'] = 0.0
    # u_b_max for winter  scaling
    self.run_options['scale_u_b_max'] = 100.0

    if steady:
      for key in steady_run_options.keys():
        self.run_options[key] = steady_run_options[key]
    else :
      for key in winter_run_options.keys():
        self.run_options[key] = winter_run_options[key]

    model_inputs = {}
    model_inputs['input_file'] = input_file
    model_inputs['out_dir'] = experiment_title + '/' + 'results_' + title
    model_inputs['constants'] = deepcopy(sim_constants)
    model_inputs['steady_file'] = '../inputs/' + experiment_title + '/' + title
    model_inputs['checkpoint_file'] = 'hdf5_results/' + title
    model_inputs['use_channels'] = False

    # Newton solver parameters
    model_inputs['newton_params'] = NonlinearVariationalSolver.default_parameters()
    model_inputs['newton_params']['newton_solver']['relaxation_parameter'] = 0.9
    model_inputs['newton_params']['newton_solver']['relative_tolerance'] = 1e-13
    model_inputs['newton_params']['newton_solver']['absolute_tolerance'] = 5e-8
    model_inputs['newton_params']['newton_solver']['error_on_nonconvergence'] = True
    model_inputs['newton_params']['newton_solver']['maximum_iterations'] = 30

    # SNES solver parameters
    model_inputs['snes_params'] = {"nonlinear_solver": "snes",
                        "snes_solver": {"linear_solver": "lu",
                        "maximum_iterations": 100,
                        "line_search": "basic",
                        "report": True,
                        "error_on_nonconvergence": True,
                        "relative_tolerance" : 1e-11,
                        "absolute_tolerance" : 1e-7}}


    self.model_inputs = model_inputs
