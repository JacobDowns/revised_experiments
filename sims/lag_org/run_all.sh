# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:26:15 2017

@author: jake
"""

for i in 0 1 2 3 4 5
do
   mpirun -np 3 python run_sim.py  $i &
done