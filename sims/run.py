## Encapsulates a single model run
import sim_constants
from winter_run_opts import *
from steady_run_opts import *

class Run(object):
  def __init__(self, title, input_file, experiment_title = '', steady = True):
    self.title = title
    self.is_steady = steady
    
    if steady :
      self.run_options = steady_run_options
    else :
      self.run_options = winter_run_options
    
    model_inputs = {}
    model_inputs['input_file'] = input_file
    model_inputs['out_dir'] = experiment_title + '/' + 'results_' + title
    model_inputs['constants'] = sim_constants
    model_inputs['steady_file'] = '../inputs/' + experiment_title + '/' + title
    model_inputs['checkpoint_file'] = 'hdf5_results/' + title 
    model_inputs['use_channels'] = False
    
    self.model_inputs = model_inputs
    