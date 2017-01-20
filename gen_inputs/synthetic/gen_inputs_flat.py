from dolfin import *
import numpy as np
from constants import *



# Directory to write model inputs
out_dir = "../../inputs/synthetic/"
# File names
out_files = [out_dir + "inputs_flat_low.hdf5", out_dir + "inputs_flat_high.hdf5"]

mesh = Mesh("../../inputs/mesh/mesh.xml")
V_cg = FunctionSpace(mesh, "CG", 1)


# Sliding speed
u_b = project(Expression("(50.0 + 250.0 * (60000.0 - x[0]) / 60000.0) / 31536000.0", degree = 1), V_cg)
# Initial sheet height
h = interpolate(Constant(0.03), V_cg)
# Initial conductivity
k = interpolate(Constant(5.2e-3), V_cg)


## Bed and surface functions

# Maximum ice thickness
h_max = 1500.
# Length of ice sheet 
length = 60e3
      
class Bed(Expression):
  def eval(self,value,x):
    value[0] = 0.0

class Surface(Expression):
  def eval(self,value,x):
    value[0] = sqrt((x[0] + 10.0) * h_max**2 / length)

# Surface
S = project(Surface(degree = 1), V_cg)
# Bed elevation
B = project(Bed(degree = 1), V_cg)
# Ice thickness
H = project(S - B, V_cg)

# High and low melt functions
ms = [project(Expression("0.5 * (1.0 + (4.0 * (60000.0 - x[0]) / 60000.0)) / 31536000.0", degree = 1), V_cg), project(Expression("(1.0 + (4.0 * (60000.0 - x[0]) / 60000.0)) / 31536000.0", degree = 1), V_cg)]


## Boundearies

# Margin
class MarginSub(SubDomain):
  def inside(self, x, on_boundary):
    return on_boundary and near(x[0], 0.0)
    
msd = MarginSub()

boundaries = FacetFunction("size_t", mesh)
boundaries.set_all(0)
msd.mark(boundaries, 1)


## Write hdf5 files
for i in range(2):
  out_file = out_files[i]
  
  # Write inputs to a hdf5 file
  f = HDF5File(mesh.mpi_comm(), out_file, 'w')
  f.write(mesh, "mesh")
  f.write(B, "B")
  f.write(H, "H")
  f.write(boundaries, "boundaries")
  f.write(u_b, "u_b_0")
  f.write(ms[i], "m_0")
  f.write(h, "h_0")
  f.write(k, "k_0")