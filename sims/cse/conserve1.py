from dolfin import *
from steady_view import *
from sim_constants import *

view = SteadyView('/home/fenics/shared/revised_experiments/inputs/ref/flat_steady.hdf5')


input_file = HDF5File(mpi_comm_world(), '/home/fenics/shared/revised_experiments/inputs/synthetic/inputs_flat_high.hdf5', 'r')

V = view.V_cg
m = Function(V)
u_b = Function(V)
boundaries = FacetFunction("size_t", view.mesh)

input_file.read(m, "m_0")
input_file.read(boundaries, "boundaries")


ds = Measure('ds', domain = view.mesh, subdomain_data = boundaries)

File('q.pvd') << view.q


A = sim_constants['A']
h_r = sim_constants['h_r']
l_r = sim_constants['l_r']



ds = Measure('ds', domain = view.mesh, subdomain_data = boundaries)

input_file.read(u_b, 'u_b_0')



print assemble(m*dx)
