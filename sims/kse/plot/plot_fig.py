# -*- coding: utf-8 -*-
"""
Custom code for plotting ref experiment figure.
"""

from pylab import *
from txt_results_reader import *

reader = TxtResultsReader('kse')
matplotlib.rcParams.update({'font.size': 14})
lw = 2.0

### Plot test point pressures

fig = figure(figsize = (12., 5))

pfos_1 = reader.pfos[0]
pfos_2 = reader.pfos[1]

colors_1 = ['r', 'g', 'b']
colors_2 = ['r--', 'g--', 'b--']
labels_1 = ['1', '2', '3']
labels_2 = ['1 Lag', '2 Lag', '3 Lag']

for j in range(3):
  plot(reader.ts, pfos_1[j,:], colors_1[j], linewidth = lw, label = labels_1[j])
  
for j in range(3):
  plot(reader.ts, pfos_2[j,:], colors_2[j], linewidth = lw, label = labels_2[j])
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('Water Pressure (Flotation Fraction)')
legend(loc=3)
grid(True)

ylim([0.73, 1.0])
  
savefig('figs/kse.png', dpi = 500)  