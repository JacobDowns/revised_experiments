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




m = vertex_to_dof_map(V_cg)
# Init vertex-edge connectivity
mesh.init(0,1)
xf = interpolate(Expression("x[0]", degree = 1), V_cg)
yf = interpolate(Expression("x[1]", degree = 1), V_cg)
f_indexes = np.loadtxt('f_indexes.txt', dtype = 'intc')






ff = FacetFunction("size_t", mesh)
File('inland_boundary.xml') >> ff

dS_inland = Measure('dS', domain = mesh, subdomain_data = ff)
n = FacetNormal(mesh)
V_tr = FunctionSpace(mesh, FiniteElement("Discontinuous Lagrange Trace", "triangle", 0))
v_tr = TestFunction(V_tr)

nxs = FacetFunction('double', mesh)
nys = FacetFunction('double', mesh)



plot = TRPlot(mesh)

flips = np.loadtxt('flips.txt')
flips_tr = Function(V_tr)
flips_tr.vector()[plot.local_facet_to_global_edge_index_map[f_indexes]] = flips

File('flip_normal.xml') << flips_tr


nxs.array()[:] = assemble(flips_tr('+')*n[0]('+')*v_tr('+')*dS_inland(1)).array()[plot.local_facet_to_global_edge_index_map]
nys.array()[:] = assemble(flips_tr('+')*n[1]('+')*v_tr('+')*dS_inland(1)).array()[plot.local_facet_to_global_edge_index_map]

np.savetxt('nxs1.txt', nxs.array()[f_indexes])
np.savetxt('nys1.txt', nys.array()[f_indexes])


File('nxs1.xml') << nxs
File('nys1.xml') << nxs
File('nxs1.pvd') << nxs
File('nys1.pvd') << nxs
