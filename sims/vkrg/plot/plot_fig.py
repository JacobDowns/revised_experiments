# -*- coding: utf-8 -*-
"""
Custom code for plotting ref experiment figure.
"""

from pylab import *
from txt_results_reader import *

reader = TxtResultsReader('vkrg')
matplotlib.rcParams.update({'font.size': 15})
lw = 2.0

### Plot test point pressures

fig = figure(figsize = (12., 5.5))

pfos = reader.pfos[0]

colors = ['r', 'g', 'b', 'k']
labels = ['1', '2', '3', '4']

for j in range(4):
  plot(reader.ts, pfos[j,:], colors[j], linewidth = lw, label = labels[j])
  
  
xlim([0.0, max(reader.ts)])
ylim([0.5, 1.0])
xlabel('Time (Months)')
ylabel('Water Pressure (Flotation Fraction)')
legend(loc = 4)
grid(True)
  
savefig('images/vkrg.png', dpi = 500)  