from time_view import *
from pylab import *

# Plot the sliding speed sensitivity experimrents

# Load hdf5 file
view_ll = TimeView('results_l_h/out.hdf5')
view_lh = TimeView('results_l_l/out.hdf5')
view_ml = TimeView('results_m_h/out.hdf5')
view_mh = TimeView('results_m_l/out.hdf5')
view_hl = TimeView('results_h_h/out.hdf5')
view_hh = TimeView('results_h_l/out.hdf5')

### Sampe N at points

Ns1 = np.zeros(view1.num_steps + view2.num_steps)
Ns2 = np.zeros(view1.num_steps + view2.num_steps)
Ns3 = np.zeros(view1.num_steps + view2.num_steps)
ts = np.zeros(view1.num_steps + view2.num_steps)

for i in range(view1.num_steps):
  print i
  N = view1.get_N(i)
  t = view1.get_t(i)

  Ns1[i] = N([10.0, 10.00])
  Ns2[i] = N([50.0, 10.00])
  Ns3[i] = N([90.0, 10.00])
  
  #ts[i] = t
  
for i in range(view2.num_steps):
  print i
  N = view2.get_N(i)
  t = view2.get_t(i)

  Ns1[view1.num_steps + i] = N([10.0, 10.00])
  Ns2[view1.num_steps + i] = N([50.0, 10.00])
  Ns3[view1.num_steps + i] = N([90.0, 10.00])
  
  #ts[view1.num_steps + i] = t

for i in range((view1.num_steps + view2.num_steps) / 365):
  ns1 = Ns1[i*365:(i+1)*365]
  plot(ns1)
  print len(ns1)  
  
#plot(ts, Ns1, 'k')
#plot(ts, Ns2, 'r')
#plot(ts, Ns3, 'b')
savefig('thing2.png')

  
  

