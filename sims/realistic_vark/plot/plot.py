from pylab import *
from constants import *

ts = loadtxt('ts.txt')
pfos1 = loadtxt('pfos.txt')
#pfos2 = loadtxt('pfos2.txt')
avg_pfos1 = loadtxt('avg_pfos.txt')
#avg_pfos2 = loadtxt('avg_pfos2.txt')
avg_ms1 = loadtxt('avg_ms.txt')
#avg_ms2 = loadtxt('avg_ms2.txt')
avg_hs1 = loadtxt('avg_hs.txt')
#avg_hs2 = loadtxt('avg_hs2.txt')
avg_ubs1 = loadtxt('avg_ubs.txt')
#avg_ubs2 = loadtxt('avg_ubs2.txt')
avg_ks1 = loadtxt('avg_ks.txt')
#avg_ks2 = loadtxt('avg_ks2.txt')


### Plot pressures at points

figure(figsize = (12, 4.5))
lw = 1.5

plot(ts, pfos1[0,:], 'r', linewidth = lw, label = '1')
plot(ts, pfos1[1,:], 'g', linewidth = lw, label = '2')
plot(ts, pfos1[2,:], 'b', linewidth = lw, label = '3')
plot(ts, pfos1[3,:], 'k', linewidth = lw, label = '4')
plot(ts, avg_pfos1, 'k--', linewidth = lw, label = 'Avg.')

#plot(ts, pfos2[0,:], 'r--', linewidth = lw, label = '1 Trough')
#plot(ts, pfos2[1,:], 'g--', linewidth = lw, label = '2 Trough')
#plot(ts, pfos2[2,:], 'b--', linewidth = lw, label = '3 Trough')

xlim([0.0, max(ts)])
ylim([0.42, 1.0])
xlabel('Time (Months)')
ylabel('Pressure (Fraction of Overburden)')
legend(loc=3, bbox_to_anchor=(0.1, 0.0))
grid(True)

savefig('images/realistic_vark.png', dpi = 500)


print str(average(avg_pfos1))
quit()

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
print "Trough average: " + str(average(avg_pfos2))
