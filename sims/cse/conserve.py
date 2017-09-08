from dolfin import *
from steady_view import *

view = SteadyView('/home/fenics/shared/revised_experiments/inputs/gse/steady.hdf5')


input_file = HDF5File(mpi_comm_world(), '/home/fenics/shared/revised_experiments/inputs/IS/inputs_is.hdf5', 'r')

V = view.V_cg
m = Function(V)
boundaries = FacetFunction("size_t", view.mesh)

input_file.read(m, "m_0")
input_file.read(boundaries, "boundaries")


ds = Measure('ds', domain = view.mesh, subdomain_data = boundaries)

print assemble(view.q*ds(0))
print assemble(view.q*ds(1))



print assemble(m*dx)
