from pylab import *
from constants import *


hrs = [0.05, 0.1, 0.5, 1, 2]

ts = loadtxt('ts.txt')
colors = ['r', 'g', 'b', 'k', 'y']
labels = [r'$h_r = 0.05 m$', r'$h_r = 0.1 m$', r'$h_r = 0.5 m$', r'$h_r = 1 m$', r'$h_r = 2 m$']


### Plot avg. pressure

figure(figsize = (12, 4.5))
lw = 2

for i in range(len(hrs)):
  hr = hrs[i]
  #pfos = loadtxt('pfos' + str(i) + '.txt')
  avg_pfos = loadtxt('avg_pfos' + str(i) + '.txt')
  print "Avg. " + str(hr) + ': ' + str(average(avg_pfos))
  #avg_ms = loadtxt('avg_ms' + str(i) + '.txt')
  #avg_hs = loadtxt('avg_hs' + str(i) + '.txt')
  #avg_ubs = loadtxt('avg_ubs' + str(i) + '.txt')
  #avg_ks = loadtxt('avg_ks' + str(i) + '.txt')
  
  plot(ts, avg_pfos, colors[i], linewidth = lw, label = labels[i])
  
xlabel('Time (Months)')
ylabel('Average Pressure (Fraction of Overburden)')
legend()
grid(True)

savefig('images/bump_sensitivity.png', dpi = 500)

### Plot inputs

figure(figsize = (12, 4.5))

subplot(3,1,1)

for i in range(len(hrs)):
  hr = hrs[i]
  avg_ms = loadtxt('avg_ms' + str(i) + '.txt')
  plot(ts, avg_ms, colors[i], linewidth = lw, label = labels[i])
    
xlabel('Time (Months)')
ylabel('Avg. m')

subplot(3,1,2)
for i in range(len(hrs)):
  hr = hrs[i]
  avg_ubs = loadtxt('avg_ubs' + str(i) + '.txt')
  plot(ts, avg_ubs, colors[i], linewidth = lw, label = labels[i])
    
xlabel('Time (Months)')
ylabel('Avg. u_b')

subplot(3,1,3)
for i in range(len(hrs)):
  hr = hrs[i]
  avg_ks = loadtxt('avg_ks' + str(i) + '.txt')
  plot(ts, avg_ks, colors[i], linewidth = lw, label = labels[i])
    
xlabel('Time (Months)')
ylabel('Avg. k')

savefig('images/inputs.png', dpi = 500)
