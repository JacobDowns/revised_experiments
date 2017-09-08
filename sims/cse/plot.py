from pylab import *

xs = loadtxt('xs.txt')
qs = loadtxt('qs.txt')
qsa = loadtxt('qsa.txt')


plot(xs, (abs(qs - qsa)/qsa)*100.0, 'ro-', linewidth = 2)
ylim([0,5])
#plot(xs, qs, 'r')
#plot(xs, qsa, 'b')
show()
