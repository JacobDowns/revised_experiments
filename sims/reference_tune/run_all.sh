for i in 0 1;
do
  mpirun -np 13 python run_sim.py $i
done    