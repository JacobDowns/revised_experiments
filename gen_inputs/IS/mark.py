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
f = Function(V_cg)
bc.apply(f.vector())

"""
class MyExp(Expression):
    def eval(self, value, x):
        value[0] = 10000.0
        value[1] = 0.0
    def value_shape(self):
        return (2,)

V_cg2 = VectorFunctionSpace(mesh, 'CG', 2)
f = project(MyExp(degree = 2), V_cg2)

print assemble(div(f)*dx)
n = FacetNormal(mesh)

print assemble(dot(f,n)*ds)

quit()"""



m = vertex_to_dof_map(V_cg)
#m1 = V_cg.dofmap().vertex_to_dof_map(mesh)

print m



# Init vertex-edge connectivity
mesh.init(0,1)
xf = interpolate(Expression("x[0]", degree = 1), V_cg)
yf = interpolate(Expression("x[1]", degree = 1), V_cg)

for i in range(5):
    f_new = np.zeros(len(f.vector().array())) #f.vector().array().copy(deepcopy = True)

    #print xf.vector().array()

    for v in vertices(mesh):
      idx = v.index()
      x0 = v.point().x()
      y0 = v.point().y()
      #print (v.point().x(), v.point().y())
      #print  - xf.vector().array()[m[idx]]
      #print v.point().y() - yf.vector().array()[m[idx]]
      #print

      neighborhood = []
      for edge in edges(v):
        for vn in vertices(edge):
          neighborhood.append(m[vn.index()])

      #print np.sqrt((x0 - xf.vector().array()[neighborhood])**2 + (y0 - yf.vector().array()[neighborhood])**2)
      #print

      #print neighborhood
      #print m[idx]

      vals = f.vector().array()[neighborhood]
      #print vals.sum()

      if vals.sum() >= 0.5:
        print "index: " + str(idx)
        f_new[m[idx]] = 1.0

    #print f_new

    f.vector()[:] = f_new


#f.vector().apply("insert")

File('f.pvd') << f
File('f.xml') << f
indicator = Function(V_cg)
indicator.vector()[:] = np.ones(len(f.vector())) - f.vector().array()

File('indicator.xml') << indicator
File('indicator.pvd') << indicator


quit()

quit()


coords = mesh.coordinates()
xs = coords[:,0]
ys = coords[:,1]

x0 = xs.min() + 0.5*(xs.max() - xs.min())
print xs.max()
print xs.min()
print x0

class Thing(SubDomain):
  def inside(self, x, on_boundary):
    return x[0] > x0

indexes = xs <= xs.max() - 5000.0
xs_margin = xs[indexes]
ys_margin = ys[indexes]

plot(xs_margin, ys_margin, 'ro-')
quit()

margin_points = zip(xs_margin, ys_margin)
line = LineString(margin_points).buffer(100)
patch = PolygonPatch(dilated, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
plot(patch)
show()


"""
ff = FacetFunction("size_t", mesh)
ff.set_all(0)
Thing().mark(ff, 1)
File('ff.pvd') << ff

ds = Measure('ds', domain = view.mesh, subdomain_data = boundaries)"""
