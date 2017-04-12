from pylab import *
from constants import *

ts = loadtxt('ts.txt')
# Only include points after melt shuts off
indexes = ts > 1.0

titles = ['low to low', 'low to high', 'medium to low', 'medium to high', 'high to low', 'high to high']

for i in range(6):
  print titles[i]
  avg_pfos = loadtxt('avg_pfos.txt')
  print ("Domain", average(avg_pfos[indexes]) / avg_pfos[0])
  
  pfos = loadtxt('pofs' + str(i) + '.txt')  
  print ('Point 1: ', average(point[0,indexes]) / pfos[0,0])
  print ('Point 2: ', average(point[1,indexes]) / pfos[1,0])
  print ('Point 3: ', average(point[2,indexes]) / pfos[2,0])
  
  print