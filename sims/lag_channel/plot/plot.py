from pylab import *
from constants import *


ts = loadtxt('ts.txt')
colors = ['r--', 'b--', 'g--', 'r', 'b', 'g']
labels = ['low_day', 'low_week', 'low_month', 'high_day', 'high_week', 'high_month']


### Plot avg. sheet height

figure(figsize = (16, 16))
lw = 2

subplot(2,1,1)

for i in range(len(labels)):
  avg_hs = loadtxt('avg_hs' + str(i) + '.txt')
  plot(ts, avg_hs, colors[i], linewidth = lw, label = labels[i])
  
xlabel('Time (Months)')
ylabel('Avg. Sheet Thickness (m)')
legend()
grid(True)



### Plot avg. pfo

subplot(2,1,2)

for i in range(len(labels)):
  avg_pfos = loadtxt('avg_pfos' + str(i) + '.txt')
  plot(ts, avg_pfos, colors[i], linewidth = lw, label = labels[i])
  
xlabel('Time (Months)')
ylabel('Average PFO')
legend()
grid(True)

savefig('images/lag.png', dpi = 500)