# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:19:13 2017

@author: jake
"""

import sys
from dolfin import MPI, mpi_comm_world
from experiment_runner import *

# Process number
MPI_rank = MPI.rank(mpi_comm_world())
experiment_title = sys.argv[1]

tune = True
if len(sys.argv) > 2 :
  tune = bool(int(sys.argv[2]))

runner = ExperimentRunner()
runner.run_all_steady(experiment_title, tune = tune)

