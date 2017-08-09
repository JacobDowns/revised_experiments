# -*- coding: utf-8 -*-

from pylab import *

x1s = loadtxt('channel/x1s.txt')
y1s = loadtxt('channel/y1s.txt')

x2s = loadtxt('channel/x2s.txt')
y2s = loadtxt('channel/y2s.txt')

S_s = loadtxt('channel/S_s.txt')

indexes = S_s > 1.0

x1s = x1s[indexes]
y1s = y1s[indexes]
x2s = x2s[indexes]
y2s = y2s[indexes]
S_s = S_s[indexes]

print max(S_s)

for i in range(len(x1s)):
  lw = S_s[i] / 4.0
  plot([x1s[i], x2s[i]], [y1s[i], y2s[i]], 'k-', lw = lw)
  
show()