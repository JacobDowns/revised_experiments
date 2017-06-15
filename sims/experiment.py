## Encapsulates a single model run
from run import *

class Experiment(object):
  
  def __init__(self, title):
    self.title = title
    self.runs = {}
    self.steady_runs = {}
    self.winter_runs = {}
  
  # Add a steady state run to the experiment
  def add_run(self, title, input_file, steady):
    run = Run(title, input_file, self.title, steady = steady)
    self.runs[title] = run
    
    if steady :
      self.steady_runs[title] = run
    else :
      self.winter_runs[title] = run
      
    return run
  
  
    