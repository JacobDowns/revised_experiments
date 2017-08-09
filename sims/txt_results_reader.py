from numpy import *
from experiment_db import *

"""
Reads text result files written by write_data.py. Useful for making plots.
"""

class TxtResultsReader(object):

  def __init__(self, experiment_title):
    # Name of experiment
    self.experiment_title = experiment_title
    # Run titles
    self.run_titles = []
    # Pressure at test points for each run
    self.pfos = []
    # Average pressures for each run
    self.avg_pfos = []
    # Average melt input for each run
    self.avg_ms = []
    # Average sheet height for each run
    self.avg_hs = []
    # Average sliding velocity for each run
    self.avg_ubs = []
    # Average conductivity for each run
    self.avg_ks = []


    for run_title, run in experiment_db[experiment_title].winter_runs.iteritems():
      self.run_titles.append(run_title)
      in_dir = '/home/fenics/shared/revised_experiments/sims/' + run.model_inputs['out_dir'] + '/txt_results/'

      self.ts = loadtxt(in_dir + 'ts.txt')
      self.pfos.append(loadtxt(in_dir + 'pfos.txt'))
      self.avg_pfos.append(loadtxt(in_dir + 'avg_pfos.txt'))
      self.avg_ms.append(loadtxt(in_dir + 'avg_ms.txt'))
      self.avg_hs.append(loadtxt(in_dir + 'avg_hs.txt'))
      self.avg_ubs.append(loadtxt(in_dir + 'avg_ubs.txt'))
      self.avg_ks.append(loadtxt(in_dir + 'avg_ks.txt'))
