"""
Runs a single model experiment. Invoked by
python run_experiment.py [experiment_name] [run_name] [tune]
"""

import sys
from dolfin import MPI, mpi_comm_world
from experiment_runner import *

# Process number
MPI_rank = MPI.rank(mpi_comm_world())
experiment_title = sys.argv[1]
run_title = sys.argv[2]

tune = True
if len(sys.argv) > 3 :
  tune = bool(int(sys.argv[3]))

runner = ExperimentRunner()
runner.run(experiment_title, run_title, tune)
