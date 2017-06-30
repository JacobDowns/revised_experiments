from pylab import *
import pickle
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import time_view as tv


### Load results file

matplotlib.rcParams.update({'font.size': 16})

view = tv.TimeView('../results_winter/hdf5_results/winter.hdf5')
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
fs = 32
matplotlib.rcParams.update({'font.size': fs})
subplot(2,1,1)

# Load a paraview color map
cdict = pickle.load(open("desaturated.p", "rb"))
desaturated = LinearSegmentedColormap('desaturated', cdict)

# Make a contour plot
cont = tricontourf(vx, vy, fi, pfo1, 100, cmap = desaturated, aspect = 'auto')

# Plot test points
borehole_xs = array([15, 30, 60, 13.13]) 
borehole_ys = array([10.4, 10.4, 10.4, 17.25]) 
plot([borehole_xs[0]], [borehole_ys[0]], 'ko', ms = 14)
plot([borehole_xs[1]], [borehole_ys[1]], 'ko', ms = 14)
plot([borehole_xs[2]], [borehole_ys[2]], 'ko', ms = 14)
plot([borehole_xs[3]], [borehole_ys[3]], 'ko', ms = 14)

bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[0] + 1.9, borehole_ys[0] + 1.5, '1', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[1] + 1.9 , borehole_ys[1] + 1.5, '2', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[2] + 1.9, borehole_ys[2] + 1.5, '3', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[3] + 1.9, borehole_ys[3] + 1.5, '4', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)




# Keep proper aspect ratio
axis('scaled')
axis('off')
xlim([-2.0, 72.0])
ylim([-2.0, 22.0])
clim(0.0, 1.0)
#colorbar(cont, ticks = linspace(0,1.0,11), fraction = 0.015, pad = 0.04)
title('(a) Summer Steady State ')
plot(xs, ys, 'k', linewidth = 2)


### Plot end of winter pressure

subplot(2,1,2)

# Hack to get the colorbar bounds correct
vx = append(vx, 1000.0)
vy = append(vy, 1000.0)
pfo2 = append(pfo2, 1.0 - 1e-16)

# Make a contour plot
cont = tricontourf(vx, vy, fi, pfo2, 100, cmap = desaturated, aspect = 'auto')

plot([borehole_xs[0]], [borehole_ys[0]], 'ko', ms = 14)
plot([borehole_xs[1]], [borehole_ys[1]], 'ko', ms = 14)
plot([borehole_xs[2]], [borehole_ys[2]], 'ko', ms = 14)
plot([borehole_xs[3]], [borehole_ys[3]], 'ko', ms = 14)

bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[0] + 1.9, borehole_ys[0] + 1.5, '1', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[1] + 1.9 , borehole_ys[1] + 1.5, '2', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[2] + 1.9, borehole_ys[2] + 1.5, '3', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)
bbox_props = dict(boxstyle="round,pad=0.275", fc="white", ec="k", lw=3, alpha = 0.8)
text(borehole_xs[3] + 1.9, borehole_ys[3] + 1.5, '4', ha = 'center', va = 'center', bbox=bbox_props, fontsize=fs)

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
plot(xs, ys, 'k', linewidth = 2)

subplots_adjust(right=0.95)
cbar_ax = fig.add_axes([0.9, 0.2, 0.015, 0.6])
cb = fig.colorbar(cont, cax = cbar_ax, ticks = linspace(0.0, 1.0, 11), label = 'Water Pressure (Flotation Fraction)')
cb.ax.tick_params(labelsize=fs) 

savefig('figs/gse.png')
#show()

