#!/bin/bash
for i in `seq 0 5`;
do
  mpirun -np 13 python run_sim.py $i
done    