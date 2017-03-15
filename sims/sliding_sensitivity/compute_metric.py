from time_view import *
from pylab import *

"""
Compute the ratio of end of winter spatially averaged PFO to summer steady state
PFO. 
"""
titles = []
titles.append("l_l")
titles.append("l_h")
titles.append("m_l")
titles.append("m_h")
titles.append("h_l")
titles.append("h_h")

for title in titles:
  view = TimeView('results_' + title + '/out.hdf5')
  print (title, view.get_avg_pfo(view.num_steps - 1) / view.get_avg_pfo(0))
  print view.get_pfo(view.num_steps - 1).vector().max()

  
  

