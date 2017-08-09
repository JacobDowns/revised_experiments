# -*- coding: utf-8 -*-
"""
Plot the summer steady state and end of winter pressures for the reference 
experiment. 
"""
import time_view as tv
from constants import *
import numpy as np
from pylab import *
from tr_plot import *

### Load results file

view = tv.TimeView('../results_winter1/hdf5_results/winter1.hdf5')
# Load the end of summer steady state pressure
pfo_first = tv.dolfin.project(view.get_pfo(0), view.V_cg)
# Load the end of winter pressure
pfo_last = view.get_pfo(view.num_steps - 1)
# Get the mesh
mesh = view.mesh

xs = tv.dolfin.project(tv.dolfin.Expression("x[0]", degree = 1), view.V_cg)
ys = tv.dolfin.project(tv.dolfin.Expression("x[1]", degree = 1), view.V_cg)

tr_plot = TRPlot(mesh)
#plot([0.0, 1.0], [1.0, 2.0], 'ko-')
#plot([3.0, 4.0], [5.0, 6.0], 'ko-')

S = tv.dolfin.Function(view.V_tr)
S.assign(view.get_S(view.num_steps-1))
ff_plot = FacetFunctionDouble(mesh)
tr_plot.copy_tr_to_facet(S, ff_plot)

i = 0


x1s = []
y1s = []
x2s = []
y2s = []
Ss = []

for f in tv.dolfin.facets(mesh):
  print i
  i += 1

  index = f.index()  
  #v1 = f.entities(0)[0]
  #v2 = f.entities(0)[1]
  
  v0 = tv.dolfin.Vertex(mesh, f.entities(0)[0])
  v1 = tv.dolfin.Vertex(mesh, f.entities(0)[1])
  
  x1 = v0.midpoint().x()
  y1 = v0.midpoint().y()
  x2 = v1.midpoint().x()
  y2 = v1.midpoint().y()
  S_val = ff_plot.array()[index]
  
  x1s.append(x1)
  y1s.append(y1)
  x2s.append(x2)
  y2s.append(y2)
  Ss.append(S_val)
  
  #plot([x1, x2], [y1, y2], ms = 0.1, lw = 0.1)
  #print (x1, y1)
  #print
  
np.savetxt('channel/x1s.txt', np.array(x1s))
np.savetxt('channel/y1s.txt', np.array(y1s))
np.savetxt('channel/x2s.txt', np.array(x2s))
np.savetxt('channel/y2s.txt', np.array(y2s))
np.savetxt('channel/S_w.txt', np.array(Ss))
  
#savefig('thing.png', dpi = 700)