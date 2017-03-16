# -*- coding: utf-8 -*-
"""
Runs the model.
"""

from dolfin import *
from dolfin import MPI, mpi_comm_world
from sheet_model import *
from sim_constants import *
from scale_functions import *

class ScaleFunctions(object):
  
  def __init__(self, model_inputs):

    # Melt
    self.m = Function(m.function_space())
    self.m.assign(m)
    # Sliding
    self.u_b = Function(u_b.function_space())
    self.u_b.assign(u_b)
    # Get function space from the melt function
    self.V_cg = m.function_space()
    # Maximum melt input
    self.m_max = m.vector().max()
    # Shutoff length
    self.shutoff_length = shutoff_length
    # Minimum conductivity
    self.k_min = k_min
    # Maximum conductivity
    self.k_max = k_max
    # Scaling parameter that sets the maximum possible conductivity
    self.a = (k_max - k_min) / (self.m_max / pcs['spy'])
    # Lag of conductivity behind melt
    self.b = lag_time
    # Parameter in the sliding speed scale function 
    self.c = (u_b_max / pcs['spy']) / self.u_b.vector().max()

    
  # Melt scale function
  def m_scale(self, t):
    if t < 0.0:
      return 1.0
    if t <= self.shutoff_length:
      return cos((pi / (2.0 * self.shutoff_length)) * t)
    return 0.0
  
  
  # Conductivity scale function
  def k_scale(self, t):
    return self.a * self.m_scale(t - self.b)


  # Sliding speed scale function
  def u_b_scale(self, t):
    return -self.m_scale(t) * (self.c - 1.0) + self.c

    
  # Gets the melt function at a particular time
  def get_m(self, t):
    return project(Constant(self.m_scale(t)) * self.m, self.V_cg)


  # Gets the conductivity function at a particular time
  def get_k(self, t):
    return project(Constant(self.k_scale(t)) * self.m + Constant(self.k_min), self.V_cg)
    
    
  # Gets the sliding speed at a particular time
  def get_u_b(self, t):
    return project(Constant(self.u_b_scale(t)) * self.u_b, self.V_cg)