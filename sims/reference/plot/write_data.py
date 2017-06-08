from time_view import *
from pylab import *
from constants import *

"""
Write data to text files for plotting -- speeds things up when lots of plot 
tweaks are needed. 
"""

### Get data

titles = ['flat1', 'trough1']

for i in range(len(titles)):
  print i
  view = TimeView('../hdf5_results/' + str(titles[i]) + '.hdf5')
  ts = view.get_ts() / pcs['spm']
  pfos = view.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])
  avg_pfos = view.get_avg_pfo_array()
  avg_ms = view.get_avg_m_array()
  avg_hs = view.get_avg_h_array()
  avg_ubs = view.get_avg_u_b_array()
  avg_ks = view.get_avg_k_array()
  
  savetxt('ts.txt', ts)
  savetxt('pfos' + str(i+1) + '.txt', pfos)
  savetxt('avg_pfos' + str(i+1) + '.txt', avg_pfos)
  savetxt('avg_ms' + str(i+1) + '.txt', avg_ms * pcs['spy'])
  savetxt('avg_ms' + str(i+1) + '.txt', avg_ms * pcs['spy'])
  savetxt('avg_hs' + str(i+1) + '.txt', avg_hs)
  savetxt('avg_ubs' + str(i+1) + '.txt', avg_ubs * pcs['spy'])
  savetxt('avg_ks' + str(i+1) + '.txt', avg_ks)

