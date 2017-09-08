from dolfin import *
from sqrt_steady_view import *
from sim_constants import *

view = SqrtSteadyView('/home/fenics/shared/revised_experiments/inputs/ref/flat_steady.hdf5')


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



#print assemble(m*dx)
#print assemble(view.q_n*ds(0))

def int_m(x):
  a = 4.22797e-8
  b = 75000.0
  l = 60000.0
  return (a*b*l - 0.5*a*l**2) - (a*b*x - 0.5*a*x**2)

import numpy as np

increments = 1500
xs = np.linspace(0.0, 60e3, increments)
q_n_int = view.width_integrate_q_n()
qs = [q_n_int([x, 20e3]) for x in xs]
qsa = np.array(map(int_m, xs))

np.savetxt('xs.txt', xs)
np.savetxt('qs.txt', qs)
np.savetxt('qsa.txt', qsa)

x = 0.0
print int_m(x)
print q_n_int([x, 20e3])
