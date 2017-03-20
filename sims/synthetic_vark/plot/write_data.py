from time_view import *
from pylab import *
from constants import *

"""
Write data to text files for plotting -- speeds things up when lots of plot 
tweaks are needed. 
"""

### Get data

view1 = TimeView('../hdf5_results/out.hdf5')
#view2 = TimeView('../hdf5_results/low.hdf5')

ts = view1.get_ts() / pcs['spm']

# Pressure at points
pfos1 = view1.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])
#pfos2 = view2.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])

# Average pressure
avg_pfos1 = view1.get_avg_pfo_array()
#avg_pfos2 = view2.get_avg_pfo_array()

# Average melt
avg_ms1 = view1.get_avg_m_array()
#avg_ms2 = view2.get_avg_m_array()

# Average sheet height
avg_hs1 = view1.get_avg_h_array()
#avg_hs2 = view2.get_avg_h_array()

# Average sliding velocity 
avg_ubs1 = view1.get_avg_u_b_array()
#avg_ubs2 = view2.get_avg_u_b_array()

# Average conductivity
avg_ks1 = view1.get_avg_k_array()
#avg_ks2 = view2.get_avg_k_array()


### Write data to text files

savetxt('ts.txt', ts)
savetxt('pfos1.txt', pfos1)
#savetxt('pfos2.txt', pfos2)
savetxt('avg_pfos1.txt', avg_pfos1)
#savetxt('avg_pfos2.txt', avg_pfos2)
savetxt('avg_ms1.txt', avg_ms1 * pcs['spy'])
#savetxt('avg_ms2.txt', avg_ms2 * pcs['spy'])
savetxt('avg_hs1.txt', avg_hs1)
#savetxt('avg_hs2.txt', avg_hs2)
savetxt('avg_ubs1.txt', avg_ubs1 * pcs['spy'])
#savetxt('avg_ubs2.txt', avg_ubs2 * pcs['spy'])
savetxt('avg_ks1.txt', avg_ks1)
#savetxt('avg_ks2.txt', avg_ks2)
