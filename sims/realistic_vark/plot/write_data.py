from time_view import *
from pylab import *
from constants import *

"""
Write data to text files for plotting -- speeds things up when lots of plot 
tweaks are needed. 
"""

### Get data

view = TimeView('../hdf5_results/out.hdf5')

# Coordinates of mesh vertices
coord = view.mesh.coordinates()
# x coords
vx = coord[:,0]
# y coords
vy = coord[:,1]
# Points to record pressure
xs = array([15, 30, 60, 13.13]) * 1000.0 + vx.min()
ys = array([10.4, 10.4, 10.4, 17.25]) * 1000.0 + vy.min()

# Times
ts = view.get_ts() / pcs['spm']
# Pressure at points
pfos = view.get_pfo_array_at_points(xs, ys)
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
savetxt('pfos.txt', pfos)
savetxt('avg_pfos.txt', avg_pfos)
savetxt('avg_ms.txt', avg_ms * pcs['spy'])
savetxt('avg_hs.txt', avg_hs)
savetxt('avg_ubs.txt', avg_ubs * pcs['spy'])
savetxt('avg_ks.txt', avg_ks)
