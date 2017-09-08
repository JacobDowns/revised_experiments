from dolfin import *
import numpy as np
from constants import *
from tr_plot import *
import numpy as np


input_file = HDF5File(mpi_comm_world(), 'domain.hdf5', 'r')
# Directory to write model inputs
out_dir = "../../inputs/IS/"

# Load mesh
mesh = Mesh()
input_file.read(mesh, "mesh", False)
V_cg = FunctionSpace(mesh, "CG", 1)

boundaries = FacetFunction("size_t", mesh)
input_file.read(boundaries, "boundaries")

bc = DirichletBC(V_cg, 1, boundaries, 1)
g = Function(V_cg)
File('f.xml') >> g




m = vertex_to_dof_map(V_cg)
# Init vertex-edge connectivity
mesh.init(0,1)
xf = interpolate(Expression("x[0]", degree = 1), V_cg)
yf = interpolate(Expression("x[1]", degree = 1), V_cg)


f_xs = []
f_ys = []
f_vx1 = []
f_vy1 = []
f_vx2 = []
f_vy2 = []
f_indexes = []
exclude_indexes = set([60914, 4418, 4420, 48932, 23863, 31736, 12065, 59216, 10083,
16127, 35596, 35593, 3896, 50118, 57557, 3943, 3951, 47964, 30946, 62019, 30837, 30838,
4076, 4071, 3920, 46628])

#print xf.vector().array()

def get_neighbors(v):
  neighborhood = []
  for e in edges(v):
    for vn in vertices(e):
      if not vn.index == v.index():
        neighborhood.append(m[vn.index()])
  return neighborhood


ff = FacetFunction("size_t", mesh)


for f in facets(mesh):

  include = True

  i = 0
  v1p = None
  v2p = None
  for v in vertices(f):
    v_index = v.index()
    v_val = g.vector().array()[m[v_index]]
    if i == 0:
      v1p = v.point()
    else :
      v2p = v.point()

    i += 1

    if v_val > 0.1:
      include = False
      break

    neighbors = get_neighbors(v)
    neighbor_vals = g.vector().array()[neighbors]
    if sum(neighbor_vals) == 0:
      include = False
      break

  if include and not f.index() in exclude_indexes:
    f_vx1.append(v1p.x())
    f_vy1.append(v1p.y())
    f_vx2.append(v2p.x())
    f_vy2.append(v2p.y())
    f_indexes.append(f.index())
    f_xs.append(f.midpoint().x())
    f_ys.append(f.midpoint().y())
    ff.array()[f.index()] = 1

import numpy as np
f_indexes = np.array(f_indexes)
f_xs = np.array(f_xs)
f_ys = np.array(f_ys)
f_vx1 = np.array(f_vx1)
f_vx2 = np.array(f_vx2)
f_vy1 = np.array(f_vy1)
f_vy2 = np.array(f_vy2)

np.savetxt('f_indexes.txt', f_indexes)
np.savetxt('f_xs.txt', f_xs)
np.savetxt('f_ys.txt', f_ys)
np.savetxt('vx1.txt', f_vx1)
np.savetxt('vy1.txt', f_vy1)
np.savetxt('vx2.txt', f_vx2)
np.savetxt('vy2.txt', f_vy2)

print np.sqrt((f_vx1 - f_vx2)**2 + (f_vy1 - f_vy2)**2).sum()



File('ff.pvd') << ff
File('inland_boundary.xml') << ff

dS_inland = Measure('dS', domain = mesh, subdomain_data = ff)
n = FacetNormal(mesh)
V_tr = FunctionSpace(mesh, FiniteElement("Discontinuous Lagrange Trace", "triangle", 0))
v_tr = TestFunction(V_tr)

print assemble(n[0]('+')*v_tr('+')*dS(1)).array()
