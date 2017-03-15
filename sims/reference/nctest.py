# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:29:23 2017

@author: jake
"""

from time_view import *

view = TimeView('results_flat/out.hdf5')
view.write_netcdf('test.nc', 'stuff')   
