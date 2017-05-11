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

# Only include points after melt shuts off
indexes = ts > 1.0

print ('Flat')
avg_pfos = avg_pfos1[indexes]
print ('Whole Domain: ', average(avg_pfos) / 0.8)
point1 = pfos1[0,indexes]
print ('Point 1: ', average(point1) / pfos1[0,0])
point2 = pfos1[1,indexes]
print ('Point 2: ', average(point2) / pfos1[1,0])
point3 = pfos1[2,indexes]
print ('Point 3: ', average(point3) / pfos1[2,0])

print 

print ('Trough')
avg_pfos = avg_pfos2[indexes]
print ('Whole Domain: ', average(avg_pfos) / 0.8)
point1 = pfos2[0,indexes]
print ('Point 1: ', average(point1) / pfos2[0,0])
point2 = pfos2[1,indexes]
print ('Point 2: ', average(point2) / pfos2[1,0])
point3 = pfos2[2,indexes]
print ('Point 3: ', average(point3) / pfos2[2,0])
