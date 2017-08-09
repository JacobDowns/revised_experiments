# -*- coding: utf-8 -*-
"""
Plot the summer steady state and end of winter pressures for the reference 
experiment. 
"""
#from dolfin import *
from pylab import *
#import dolfin as dolfin
import pickle
from matplotlib.colors import LinearSegmentedColormap
import time_view as tv
from constants import *
import numpy as np

### Load results file

view = tv.TimeView('../results_winter1/hdf5_results/winter1.hdf5')
# Load the end of summer steady state pressure
pfo_first = tv.dolfin.project(view.get_pfo(0), view.V_cg)
# Load the end of winter pressure
pfo_last = view.get_pfo(view.num_steps - 1)
# Get the mesh
mesh = view.mesh


### Set up some stuff for plotting

# Load mesh boundary contour
cont = np.loadtxt("IS_cont_50.txt")
xs = cont[:,0]
ys = cont[:,1]

# Coordinates of mesh vertices
coord = mesh.coordinates()
# x coords
vx = coord[:,0]
# y coords
vy = coord[:,1]
# Index of vertices that form triangles
fi = mesh.cells()

# Do some rescaling and translation of the domain
vx_min = vx.min()
vy_min = vy.min()
vx -= vx_min
vy -= vy_min
vx /= 1000.0
vy /= 1000.0
xs -= vx_min
ys -= vy_min
xs /= 1000.0
ys /= 1000.0
xs = np.append(xs, xs[0])
ys = np.append(ys, ys[0])

# Get pressure values as arrays
pfo1 = pfo_first.compute_vertex_values(mesh)
pfo2 = pfo_last.compute_vertex_values(mesh)
# pfo is a miniscule fraction above overburden so clip it
pfo1[pfo1 > 1.0] = 1.0
pfo2[pfo2 > 1.0] = 1.0


### Plot the steady state pressure

fig = figure(figsize = (26,13.5))
fs = 20
matplotlib.rcParams.update({'font.size': fs})
subplot(2,1,1)

# Load a paraview color map
cdict = pickle.load(open("desaturated.p", "rb"))
desaturated = LinearSegmentedColormap('desaturated', cdict)

# Make a contour plot
cont = tricontourf(vx, vy, fi, pfo1, 200, cmap = desaturated, aspect = 'auto')
# Keep proper aspect ratio
axis('scaled')
axis('off')
xlim([-2.0, 72.0])
ylim([-2.0, 22.0])
clim(0.0, 1.0)
#colorbar(cont, ticks = linspace(0,1.0,11), fraction = 0.015, pad = 0.04)
title('(a) End of Summer')


x1s = loadtxt('channel/x1s.txt')
y1s = loadtxt('channel/y1s.txt')

x2s = loadtxt('channel/x2s.txt')
y2s = loadtxt('channel/y2s.txt')

S_s = loadtxt('channel/S_s.txt')

indexes = S_s > 0.01

x1s = x1s[indexes] / 1000.0
y1s = y1s[indexes] / 1000.0
x2s = x2s[indexes] / 1000.0
y2s = y2s[indexes] / 1000.0
S_s = S_s[indexes]

print max(S_s)

for i in range(len(x1s)):
  print i
  lw = min(S_s[i] / 5.0, 3)
  plot([x1s[i], x2s[i]], [y1s[i], y2s[i]], 'k-', lw = lw)

xs = [0.0, 60.0, 60.0, 0., 0.0]
ys = [0.0, 0.0, 20.0, 20.0, 0.0]
plot(xs, ys, 'k', linewidth = 2)

# Plot test points
borehole_xs = array([10., 20., 50.]) 
borehole_ys = array([10., 10., 10.]) 

scatter(borehole_xs, borehole_ys, s=110, c='k', edgecolors='w', linewidth = 1, zorder=10)
bbox_props = dict(boxstyle="round,pad=0.32", fc="white", ec="k", lw=1.5, alpha = 1.)
text(borehole_xs[0] + 1.5, borehole_ys[0] + 1.5, '1', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.32", fc="white", ec="k", lw=1.5, alpha = 1.)
text(borehole_xs[1] + 1.5 , borehole_ys[1] + 1.5, '2', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.32", fc="white", ec="k", lw=1.5, alpha = 1.)
text(borehole_xs[2] + 1.5, borehole_ys[2] + 1.5, '3', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)


### Plot end of winter pressure

subplot(2,1,2)

# Hack to get the colorbar bounds correct
vx = append(vx, 1000.0)
vy = append(vy, 1000.0)
pfo2 = append(pfo2, 1.0 - 1e-16)

# Make a contour plot
cont = tricontourf(vx, vy, fi, pfo2, 200, cmap = desaturated, aspect = 'auto')
# Keep proper aspect ratio
axis('scaled')
axis('off')
#xlabel('x (km)')
#ylabel('y (km)')
xlim([-2.0, 72.0])
ylim([-2.0, 22.0])
clim(0.0, 1.0)
#colorbar(cont, ticks = linspace(0,1.0,11), fraction = 0.05, pad = 0.04, orientation='horizontal')
title('(b) End of Winter')
xs = [0.0, 60.0, 60.0, 0., 0.0]
ys = [0.0, 0.0, 20.0, 20.0, 0.0]
plot(xs, ys, 'k', linewidth = 2)

scatter(borehole_xs, borehole_ys, s=110, c='k', edgecolors='w', linewidth = 1)
bbox_props = dict(boxstyle="round,pad=0.32", fc="white", ec="k", lw=2, alpha = 1.)
text(borehole_xs[0] + 1.5, borehole_ys[0]+ 1.5, '1', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2, alpha = 1.)
text(borehole_xs[1] + 1.5 , borehole_ys[1] + 1.5, '2', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2, alpha = 1.)
text(borehole_xs[2] + 1.5, borehole_ys[2] + 1.5, '3', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)


x1s = loadtxt('channel/x1s.txt')
y1s = loadtxt('channel/y1s.txt')

x2s = loadtxt('channel/x2s.txt')
y2s = loadtxt('channel/y2s.txt')

S_w = loadtxt('channel/S_w.txt')

indexes = S_w > 0.01

x1s = x1s[indexes] / 1000.0
y1s = y1s[indexes] / 1000.0
x2s = x2s[indexes] / 1000.0
y2s = y2s[indexes] / 1000.0
S_w = S_w[indexes]

print max(S_w)

for i in range(len(x1s)):
  print i
  lw = min(S_w[i] / 5.0, 3)
  plot([x1s[i], x2s[i]], [y1s[i], y2s[i]], 'k-', lw = lw)

subplots_adjust(right=0.95)
cbar_ax = fig.add_axes([0.9, 0.2, 0.015, 0.6])
cb = fig.colorbar(cont, cax = cbar_ax, ticks = linspace(0.0, 1.0, 11), label = 'Water Pressure (Flotation Fraction)')
cb.ax.tick_params(labelsize=fs) 

savefig('images/cse.png', dpi=500)
#show()

