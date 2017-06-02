from pylab import *
from constants import *


ts = loadtxt('ts.txt')
colors = ['r--', 'b--', 'g--', 'r', 'b', 'g']
labels = ['low: 1 day', 'low: 2 day', 'low: week', 'high: 1 day', 'high: 2 day', 'high: week'] 



### Plot avg. pressure

figure(figsize = (12, 4.5))
lw = 2

for i in range(len(labels)):
  avg_pfos = loadtxt('avg_pfos' + str(i) + '.txt')
  plot(ts, avg_pfos, colors[i], linewidth = lw, label = labels[i])

ylim([0.35, 0.85])
xlabel('Time (Months)')
ylabel('Spatially Averaged Pressure (Flotation Fraction)')
legend(loc=4)
grid(True)
savefig('images/lag_pressure.png', dpi = 500)



### Plot avg. sheet height
figure(figsize = (12, 4.5))
lw = 2

for i in range(len(labels)):
  avg_hs = loadtxt('avg_hs' + str(i) + '.txt')
  plot(ts, avg_hs, colors[i], linewidth = lw, label = labels[i])

xlabel('Time (Months)')
ylabel('Spatially Averaged Sheet Thickness (m)')
legend()
grid(True)
savefig('images/lag_sheet.png', dpi = 500)

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