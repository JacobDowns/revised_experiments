from pylab import *
from constants import *

### Plot avg. pressure

figure(figsize = (12, 8.5))
lw = 2
ts = loadtxt('ts.txt')
labels = [r'$l \to l$', r'$l \to h$', r'$m \to l$', r'$m \to h$', r'$h \to l$', r'$h \to h$']
titles = ['Slow Summer', 'Moderate Summer', 'Fast Summer']

for i in range(3):
  subplot(3,1,i+1)
  title(titles[i])
  avg_pfos1 = loadtxt('avg_pfos' + str(2*i) + '.txt')
  avg_pfos2 = loadtxt('avg_pfos' + str(2*i + 1) + '.txt')
  
  #print len(ts)
  #print len(avg_pfos1)
  #print len(avg_pfos2)
  #quit()
  
  plot(ts, avg_pfos1, 'k', linewidth = lw, label = 'Slow Winter')
  plot(ts, avg_pfos2, 'k--', linewidth = lw, label = 'Fast Winter')
  
  yticks([0.0, 0.25, 0.5, 0.75, 1.0])
  
  if i == 2:
    xlabel('Time (Months)')
  if i == 1:
    ylabel('Average Pressure (Fraction of Overburden)')
  legend()
  grid(True)

savefig('images/sliding_sensitivity.png', dpi = 500)
tight_layout()

quit()


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


"""
### Plot pressures at points



plot(ts, pfos1[0,:], 'r', linewidth = lw, label = '1 Flat')
plot(ts, pfos1[1,:], 'g', linewidth = lw, label = '2 Flat')
plot(ts, pfos1[2,:], 'b', linewidth = lw, label = '3 Flat')

plot(ts, pfos2[0,:], 'r--', linewidth = lw, label = '1 Trough')
plot(ts, pfos2[1,:], 'g--', linewidth = lw, label = '2 Trough')
plot(ts, pfos2[2,:], 'b--', linewidth = lw, label = '3 Trough')

xlim([0.0, max(ts)])
xlabel('Time (Months)')
ylabel('Pressure (Fraction of Overburden)')
legend()
grid(True)

savefig('images/ref.png', dpi = 500)


### Plot melt, u_b, and k

figure(figsize = (12, 4.5))

subplot(3,1,1)
plot(ts, avg_ms1, 'k', linewidth = lw, label = 'Flat')
plot(ts, avg_ms2, 'k--', linewidth = lw, label = 'Trough')
xlabel('Time (Months)')
ylabel('Avg. m')
legend()

subplot(3,1,2)
plot(ts, avg_ubs1, 'k', linewidth = lw, label = 'Flat')
plot(ts, avg_ubs2, 'k--', linewidth = lw, label = 'Trough')
xlabel('Time (Months)')
ylabel('Avg. u_b')
legend()

subplot(3,1,3)
plot(ts, avg_ks1, 'k', linewidth = lw, label = 'Flat')
plot(ts, avg_ks2, 'k--', linewidth = lw, label = 'Trough')
xlabel('Time (Months)')
ylabel('Avg. k')
legend()

savefig('images/inputs.png', dpi = 500)
tight_layout()


### Compute the average winter pressure (average in time and space)

print "Flat average: " + str(average(avg_pfos1))
print "Trough average: " + str(average(avg_pfos2))"""
