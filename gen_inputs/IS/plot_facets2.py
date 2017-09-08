from pylab import *

f_indexes = loadtxt('f_indexes.txt')
f_xs = loadtxt('f_xs.txt')
f_ys = loadtxt('f_ys.txt')

vx1 = loadtxt('vx1.txt')
vy1 = loadtxt('vy1.txt')
vx2 = loadtxt('vx2.txt')
vy2 = loadtxt('vy2.txt')
nxs = loadtxt('nxs1.txt')
nys = loadtxt('nys1.txt')


for i in range(len(f_indexes)):
  index = int(f_indexes[i])
  plot([vx1[i], vx2[i]], [vy1[i], vy2[i]], 'ko-')
  #plot([f_xs[i]], [f_ys[i]], 'ko', ms = 5)
  text(f_xs[i], f_ys[i], str(int(f_indexes[i])))

  plot([f_xs[i], f_xs[i] + nxs[i]], [f_ys[i], f_ys[i] + nys[i]], 'ro-')

show()
