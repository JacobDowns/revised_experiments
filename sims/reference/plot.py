from time_view import *
from pylab import *

"""
Plot pressure for the flat bed and trough runs.
"""

view_flat = TimeView('results_flat/out.hdf5')

for title in titles:
  view = TimeView('results_' + title + '/out.hdf5')
  print (title, view.get_avg_pfo(view.num_steps - 1) / view.get_avg_pfo(0))
  print view.get_pfo(view.num_steps - 1).vector().max()
