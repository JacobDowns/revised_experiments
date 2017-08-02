# -*- coding: utf-8 -*-
"""
Custom code for plotting ref experiment figure.
"""

from pylab import *
from txt_results_reader import *

reader = TxtResultsReader('ref')
matplotlib.rcParams.update({'font.size': 15})
lw = 2.0

### Plot test point pressures

fig = figure(figsize = (12., 5.2))

pfos_f = reader.pfos[0]
pfos_t = reader.pfos[1]

colors_f = ['r', 'g', 'b']
colors_t = ['r--', 'g--', 'b--']
labels_f = ['1 Flat', '2 Flat', '3 Flat']
labels_t = ['1 Trough', '2 Trough', '3 Trough']

for j in range(3):
  plot(reader.ts, pfos_f[j,:], colors_f[j], linewidth = lw, label = labels_f[j])
  
for j in range(3):
  plot(reader.ts, pfos_t[j,:], colors_t[j], linewidth = lw, label = labels_t[j])
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('Water Pressure (Flotation Fraction)')
legend()
grid(True)
  
savefig('images/ref.png', dpi = 500)  