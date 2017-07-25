# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:42:36 2016
@author: jake
"""
from dolfin import *
from constants import *

class ScaleFunctions(object):
  
  def __init__(self, m, u_b, run):

    # Melt
    self.m = Function(m.function_space())
    self.m.assign(m)
    # Sliding
    self.u_b = Function(u_b.function_space())
    self.u_b.assign(u_b)
    # Get function space from the melt function
    self.V_cg = m.function_space()
    # Maximum melt input
    self.m_max = run.run_options['scale_k_min'] / pcs['spy']
    # Shutoff length
    self.shutoff_length = run.run_options['scale_shutoff_length']
    # Minimum conductivity
    self.k_min = run.run_options['scale_k_min']
    # Maximum conductivity
    self.k_max = run.run_options['scale_k_max']
    # Lag of conductivity behind melt
    self.l = run.run_options['scale_k_lag']
    # Parameter in the sliding speed scale function 
    self.c = (run.run_options['scale_u_b_max'] / pcs['spy']) / self.u_b.vector().max()
    # Background basal melt
    self.m_min = run.run_options['scale_m_min']
    
    def default_m_scale(t):
      if t < 0.0:
        return 1.0
      if t <= self.shutoff_length:
        return cos((pi / (2.0 * self.shutoff_length)) * t)
      return 0.0
    # Function for scaling melt
    if 'scale_m_scale' in run.run_options :
      self.m_scale = run.run_options['scale_m_scale']
    else :
      self.m_scale = default_m_scale
  
  # Conductivity scale function
  def k_scale(self, t):
    return ((self.k_max - self.k_min) / self.m_max) * self.m_scale(t - self.l)


  # Sliding speed scale function
  def u_b_scale(self, t):
    return -self.m_scale(t) * (self.c - 1.0) + self.c

    
  # Gets the melt function at a particular time
  def get_m(self, t):
    return project(Constant(self.m_scale(t)) * self.m + Constant(self.m_min), self.V_cg)


  # Gets the conductivity function at a particular time
  def get_k(self, t):
    return project(Constant(self.k_scale(t)) * self.m + Constant(self.k_min), self.V_cg)
    
    
  # Gets the sliding speed at a particular time
  def get_u_b(self, t):
    return project(Constant(self.u_b_scale(t)) * self.u_b, self.V_cg)