
for i in 0 1 2 3 4 5
do
  mpirun -np 7 python run_sim.py $i &
  sleep 20
done