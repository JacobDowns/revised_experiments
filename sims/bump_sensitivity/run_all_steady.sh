#!/bin/bash
for i in `seq 0 4`;
do
  mpirun -np 13 python run_sim_steady.py $i
done    