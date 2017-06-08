from pylab import *
from constants import *

figure(figsize = (12, 4.5))
lw = 1.5

ts = loadtxt('ts.txt')
titles = ['no_void', 'low_void', 'high_void']
colors = ['r', 'g', 'b']

for i in range(len(titles)):
  title = titles[i]
  
  avg_pfos = loadtxt('avg_pfos' + str(i+1) + '.txt')
  plot(ts, avg_pfos, color = colors[i], linewidth = lw)

savefig('images/pressure_sheet_storage.png', dpi = 500)
