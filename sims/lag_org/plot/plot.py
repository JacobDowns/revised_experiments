from pylab import *
from constants import *


ts = loadtxt('ts.txt')
colors = ['r', 'b', 'g', 'r--', 'b--', 'g--']
labels = ['low_day', 'low_week', 'low_month', 'high_day', 'high_week', 'high_month']


### Plot avg. pressure


figure(figsize = (12, 4.5))
lw = 2

for i in range(len(labels)):
  #avg_hs = loadtxt('avg_hs' + str(i) + '.txt')
  #plot(ts, avg_hs, colors[i], linewidth = lw, label = labels[i])
  
  pfos = loadtxt('pfos' + str(i) + '.txt')
  plot(ts, pfos[1,:], linewidth = lw, label = labels[i] + ' 1')
  #plot(ts, pfos[1,:], linewidth = lw, label = labels[i] + ' 2')
  #plot(ts, pfos[2,:], 'b', linewidth = lw, label = labels[i] + ' 3')

xlabel('Time (Months)')
#ylabel('Average Sheet Thickness (m)')
legend()
grid(True)

savefig('images/lag.png', dpi = 500)


"""
figure(figsize = (12, 4.5))
lw = 2

subplot(3,1,1)
for i in range(len(labels)):
  avg_ms = loadtxt('avg_ms' + str(i) + '.txt')
  plot(ts, avg_ms, linewidth = lw, label = labels[i])
  xlabel('Time (Months)')
  ylabel('Avg. m')
  legend()

subplot(3,1,2)
for i in range(len(labels)):
  avg_ubs = loadtxt('avg_ubs' + str(i) + '.txt')
  plot(ts, avg_ubs, linewidth = lw, label = labels[i])
  xlabel('Time (Months)')
  ylabel('Avg. u_b')
  legend()

subplot(3,1,3)
for i in range(len(labels)):
  avg_ks= loadtxt('avg_ks' + str(i) + '.txt')
  plot(ts, avg_ks, linewidth = lw, label = labels[i])
  xlabel('Time (Months)')
  ylabel('Avg. k')
  legend()

savefig('images/inputs.png', dpi = 500)
tight_layout()"""