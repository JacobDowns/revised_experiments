from pylab import *
from constants import *

ts = loadtxt('flat/ts.txt')
# Only include points after melt shuts off
indexes = ts > 1.0

titles = ['flat', 'trough']

for i in range(6):
  title = titles[i]
  print title
  avg_pfos = loadtxt(title + '/avg_pfos1.txt')
  print ("Domain", average(avg_pfos[indexes]) / avg_pfos[0])
  
  pfos = loadtxt(title + '/pfos1' + str(i) + '.txt')  
  print ('Point 1: ', average(point[0,indexes]) / pfos[0,0])
  print ('Point 2: ', average(point[1,indexes]) / pfos[1,0])
  print ('Point 3: ', average(point[2,indexes]) / pfos[2,0])
  
  print