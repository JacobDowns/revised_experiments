"""
Performs all winter runs in an experiment. Invoked by
python run_all_winter.py [experiment_name] [n]
where n is the number of processors to use.
"""

import sys
from experiment_db import *
from subprocess import call

# Experiment to run
experiment_title = sys.argv[1]
# Number of processors
n = sys.argv[2]

experiment = experiment_db[experiment_title]

for run_title in experiment.winter_runs.keys():
  call(["mpirun -np " + str(n) + " python run_experiment.py " + experiment_title + " " + run_title], shell=True)
  print
