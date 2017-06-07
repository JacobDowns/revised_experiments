from pylab import *
from constants import *

ts = loadtxt('flat/ts.txt')
# Only include points after melt shuts off
indexes = ts > 1.0

titles = ['flat']

for title in titles:
  print title
  avg_pfos = loadtxt(title + '/avg_pfos.txt')
  print ("Domain", average(avg_pfos[indexes]) / avg_pfos[0])

  pfos = loadtxt(title + '/pfos.txt')  
  
  p1 = average(pfos[0,indexes]) / pfos[0,0]
  print ('Point 1: ', p1)
  
  p2 = average(pfos[1,indexes]) / pfos[1,0]
  print ('Point 2: ', p2)
  
  p3 = average(pfos[2,indexes]) / pfos[2,0]
  print ('Point 3: ', p3)
  
  print