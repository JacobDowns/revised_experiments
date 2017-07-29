from dolfin import *
from time_view import *

  
view = TimeView('steady1.hdf5')

# Times
ts = view.get_ts() 
phi = Function(view.V_cg)
phi_m = Function(view.V_cg)
out = File('phi/phi.pvd')

for i in range(len(ts)):
  print i
  print
  phi.assign(view.get_phi(i))
  phi_m.assign(project(dot(grad(phi), grad(phi)), view.V_cg))
  out << phi