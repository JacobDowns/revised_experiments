from pylab import *
from constants import *

ts = loadtxt('ts.txt')
pfos = loadtxt('pfos.txt')
avg_pfos = loadtxt('avg_pfos.txt')
avg_ms = loadtxt('avg_ms.txt')
avg_hs = loadtxt('avg_hs.txt')
avg_ubs = loadtxt('avg_ubs.txt')
avg_ks = loadtxt('avg_ks.txt')

# Only include points after melt shuts off
indexes = ts > 1.0

avg_pfos = avg_pfos[indexes]
print ('Whole Domain: ', average(avg_pfos) / 0.8)
point1 = pfos[0,indexes]
print ('Point 1: ', average(point1) / pfos[0,0])
point2 = pfos[1,indexes]
print ('Point 2: ', average(point2) / pfos[1,0])
point3 = pfos[2,indexes]
print ('Point 3: ', average(point3) / pfos[2,0])
point4 = pfos[3,indexes]
print ('Point 4: ', average(point4) / pfos[3,0])

