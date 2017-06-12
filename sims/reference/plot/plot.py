from pylab import *
from constants import *

ts = loadtxt('ts.txt')
pfos1 = loadtxt('pfos1.txt')
pfos2 = loadtxt('pfos2.txt')
avg_pfos1 = loadtxt('avg_pfos1.txt')
avg_pfos2 = loadtxt('avg_pfos2.txt')
avg_ms1 = loadtxt('avg_ms1.txt')
avg_ms2 = loadtxt('avg_ms2.txt')
avg_hs1 = loadtxt('avg_hs1.txt')
avg_hs2 = loadtxt('avg_hs2.txt')
avg_ubs1 = loadtxt('avg_ubs1.txt')
avg_ubs2 = loadtxt('avg_ubs2.txt')
avg_ks1 = loadtxt('avg_ks1.txt')
avg_ks2 = loadtxt('avg_ks2.txt')

print avg_ms1
print
print avg_ms2
quit()

### Plot pressures at points

fig = figure(figsize = (13., 5.5))
matplotlib.rcParams.update({'font.size': 16})
lw = 2.5

plot(ts, pfos1[0,:], 'r', linewidth = lw, label = '1 Flat')
plot(ts, pfos1[1,:], 'g', linewidth = lw, label = '2 Flat')
plot(ts, pfos1[2,:], 'b', linewidth = lw, label = '3 Flat')

plot(ts, pfos2[0,:], 'r--', linewidth = lw, label = '1 Trough')
plot(ts, pfos2[1,:], 'g--', linewidth = lw, label = '2 Trough')
plot(ts, pfos2[2,:], 'b--', linewidth = lw, label = '3 Trough')

xlim([0.0, max(ts)])
xlabel('Time (Months)')
ylabel('Water Pressure (Flotation Fraction)')
legend()
grid(True)
xlim([0,8])

savefig('images/ref1', dpi = 500)
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