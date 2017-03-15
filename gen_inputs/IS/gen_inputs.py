from dolfin import *
import numpy as np
from constants import *

input_file = HDF5File(mpi_comm_world(), 'domain.hdf5', 'r') 
# Directory to write model inputs
out_dir = "../../inputs/IS/"

# Load mesh
mesh = Mesh()
input_file.read(mesh, "mesh", False)  
V_cg = FunctionSpace(mesh, "CG", 1)

# Bed elevation
B = Function(V_cg)
input_file.read(B, "B")

# Ice thickness
H = Function(V_cg)
input_file.read(H, "H")

# Sliding speed 
u_b = Function(V_cg)
input_file.read(u_b, "u_b_0")

# Melt
m = Function(V_cg)
input_file.read(m, "m_0")

# Dirichlet boundaries
boundaries = FacetFunction("size_t", mesh)
input_file.read(boundaries, "boundaries")

# Initial sheet height
h = interpolate(Constant(0.03), V_cg)

# Initial conductivity
k = interpolate(Constant(5e-3), V_cg)

# Write inputs to a hdf5 file
out_file = out_dir + 'inputs_is.hdf5'
f = HDF5File(mesh.mpi_comm(), out_file, 'w')
f.write(mesh, "mesh")
f.write(B, "B")
f.write(H, "H")
f.write(boundaries, "boundaries")
f.write(u_b, "u_b_0")
f.write(m, "m_0")
f.write(h, "h_0")
f.write(k, "k_0")