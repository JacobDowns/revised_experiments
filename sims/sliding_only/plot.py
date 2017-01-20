# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:23:56 2017

@author: jake
"""

from sqrt_steady_view import *
from pylab import *

# Load hdf5 file
view = SqrtSteadyView('../../inputs/steady_sliding_only/steady_flat_high.hdf5')

avg_pfo = view.avg_pfo()

  

