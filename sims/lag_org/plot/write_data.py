from time_view import *
from pylab import *
from constants import *

"""
Write data to text files for plotting -- speeds things up when lots of plot 
tweaks are needed. 
"""

### Get data

labels = ['low_day', 'low_week', 'low_month', 'high_day', 'high_week', 'high_month']
#labels = ['low_day', 'low_month', 'high_day', 'high_week', 'high_month']


#labels = ['low_week']

for i in range(len(labels)):
  print i 
  label = labels[i]
  view = TimeView('../hdf5_results/' + labels[i] + '.hdf5')

  # Times
  ts = view.get_ts() / pcs['spm']
  # Pressure at points
  pfos = view.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])
  # Average pressure
  avg_pfos = view.get_avg_pfo_array()
  # Average melt
  avg_ms = view.get_avg_m_array()
  # Average sheet height
  avg_hs = view.get_avg_h_array()
  # Average sliding velocity 
  avg_ubs = view.get_avg_u_b_array()
  # Average conductivity
  avg_ks = view.get_avg_k_array()
  
  savetxt('ts.txt', ts)
  savetxt('pfos' + str(i) + '.txt', pfos)
  savetxt('avg_pfos' + str(i) + '.txt', avg_pfos)
  savetxt('avg_ms' + str(i) + '.txt', avg_ms * pcs['spy'])
  savetxt('avg_hs' + str(i) + '.txt', avg_hs)
  savetxt('avg_ubs' + str(i) + '.txt', avg_ubs * pcs['spy'])
  savetxt('avg_ks' + str(i) + '.txt', avg_ks)


