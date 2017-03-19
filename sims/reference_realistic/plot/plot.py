from pylab import *
from constants import *

ts = loadtxt('ts.txt')
pfos = loadtxt('pfos.txt')
avg_pfos = loadtxt('avg_pfos.txt')
avg_ms = loadtxt('avg_ms.txt')
avg_hs = loadtxt('avg_hs.txt')
avg_ubs = loadtxt('avg_ubs.txt')
avg_ks = loadtxt('avg_ks.txt')


### Plot pressures at points

figure(figsize = (12, 4.5))
lw = 1.5

plot(ts, pfos[0,:], 'r', linewidth = lw, label = '1')
plot(ts, pfos[1,:], 'g', linewidth = lw, label = '2')
plot(ts, pfos[2,:], 'b', linewidth = lw, label = '3')
plot(ts, pfos[3,:], 'k', linewidth = lw, label = '4')
plot(ts, avg_pfos, 'k--', linewidth = lw, label = 'Avg.')


ylim([0.3, 1.0])
xlim([0.0, max(ts)])
xlabel('Time (Months)')
ylabel('Pressure (Fraction of Overburden)')
legend(loc=5)
grid(True)

savefig('images/ref_is.png', dpi = 500)


### Plot melt, u_b, and k

figure(figsize = (12, 4.5))

subplot(3,1,1)
plot(ts, avg_ms, 'k', linewidth = lw)
xlabel('Time (Months)')
ylabel('Avg. m')

subplot(3,1,2)
plot(ts, avg_ubs, 'k', linewidth = lw)
xlabel('Time (Months)')
ylabel('Avg. u_b')

subplot(3,1,3)
plot(ts, avg_ks, 'k', linewidth = lw)
xlabel('Time (Months)')
ylabel('Avg. k')

savefig('images/inputs.png', dpi = 500)
tight_layout()


### Compute the average winter pressure (average in time and space)

print "Avg.: " + str(average(avg_pfos))
