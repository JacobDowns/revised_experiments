from pylab import *
from constants import *

ts = loadtxt('ts.txt')
# Only include points after melt shuts off
indexes = ts > 1.0

titles = ['low to low', 'low to high', 'medium to low', 'medium to high', 'high to low', 'high to high']

avgs = []
p1s = []
p2s = []
p3s = []

for i in range(6):
  print titles[i]
  avg_pfos = loadtxt('avg_pfos' + str(i) + '.txt')
  avg = average(avg_pfos[indexes]) / avg_pfos[0]
  avgs.append(avg)
  print ("Domain", avg)

  
  pfos = loadtxt('pfos' + str(i) + '.txt')  
  
  p1 = average(pfos[0,indexes]) / pfos[0,0]
  p1s.append(p1)
  print ('Point 1: ', p1)
  
  p2 = average(pfos[1,indexes]) / pfos[1,0]
  p2s.append(p2)
  print ('Point 2: ', p2)
  
  p3 = average(pfos[2,indexes]) / pfos[2,0]
  p3s.append(p3)
  print ('Point 3: ', p3)
  
  print
  
print 

print ("Domain range", min(avgs), max(avgs))
print ("Point 1 range", min(p1s), max(p1s))
print ("Point 2 range", min(p2s), max(p2s))
print ("Point 3 range", min(p3s), max(p3s))