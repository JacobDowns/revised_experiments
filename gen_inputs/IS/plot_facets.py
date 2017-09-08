from pylab import *

f_indexes = loadtxt('f_indexes.txt')
f_xs = loadtxt('f_xs.txt')
f_ys = loadtxt('f_ys.txt')

vx1 = loadtxt('vx1.txt')
vy1 = loadtxt('vy1.txt')
vx2 = loadtxt('vx2.txt')
vy2 = loadtxt('vy2.txt')

exclude_indexes = set([60914, 4418, 4420, 48932, 23863, 31736, 12065, 59216, 10083,
16127, 35596, 35593, 3896, 50118, 57557, 3943, 3951, 47964, 30946, 62019, 30837, 30838,
4076, 4071, 3920, 46628])

for i in range(len(f_indexes)):
  index = int(f_indexes[i])
  if not index in exclude_indexes:
    plot([vx1[i], vx2[i]], [vy1[i], vy2[i]], 'ko-')
    text(f_xs[i], f_ys[i], str(int(f_indexes[i])))

show()
