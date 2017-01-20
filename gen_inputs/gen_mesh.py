# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:30:59 2017

@author: jake
"""

from dolfin import *
from mshr import *

# Create geometry
domain = Rectangle(dolfin.Point(0., 0.), dolfin.Point(60e3, 20e3))
# Create mesh (around 200 - 250m resolution)
mesh = generate_mesh(domain, 140)
# Save to file and plot
File("../inputs/mesh/mesh.xml") << mesh
