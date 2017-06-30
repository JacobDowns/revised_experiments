# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:47:40 2017

@author: jake
"""

from dolfin import *
from time_view import *
from pylab import *

view = TimeView('results_l_void_winter/hdf5_results/l_void_winter.hdf5')


# Times
ts = view.get_ts() / pcs['spm']
hes = []

for i in range(len(ts)):
  print ts[i]
  avg_h_e = assemble(Constant(1e-4/ (1000.0 * 9.8)) * (view.get_pfo(i) * view.phi0)*dx(view.mesh)) / assemble(1.0 * dx(view.mesh))
  print avg_h_e  
  print
  hes.append(avg_h_e)  
  
plot(ts, hes)
savefig('thing.png')

print "Max: " + str(max(hes))
print "Min: " + str(min(hes))
print "Drop: " + str(max(hes) - min(hes))
d = max(hes) - min(hes)

print "Rate: " +  str(d / (3./4.))

