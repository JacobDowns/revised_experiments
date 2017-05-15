from pylab import *
from constants import *


ts = loadtxt('ts.txt')
colors = ['r', 'b', 'g', 'r--', 'b--', 'g--']
labels = ['low_day_lag', 'low_week_lag', 'low_month_lag', 'high_day_lag', 'high_week_lag', 'high_month_lag']


### Plot avg. pressure

figure(figsize = (12, 4.5))
lw = 2

for i in range(len(labels)):
  avg_hs = loadtxt('avg_hs' + str(i) + '.txt')
  plot(ts, avg_hs, colors[i], linewidth = lw, label = labels[i])
  
xlabel('Time (Months)')
ylabel('Average Sheet Thickness (m)')
legend()
grid(True)

savefig('images/lag.png', dpi = 500)