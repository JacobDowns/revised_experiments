from dolfin import *
from time_view import *
from pylab import *
from sim_constants import *
from experiment_db import *
import sys
import os

"""
Write data to text files for plotting -- speeds things up when lots of plot 
tweaks are needed. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())
experiment_title = sys.argv[1]

realistic = False
if len(sys.argv) > 2 :
  realistic = bool(int(sys.argv[2]))

def write_run(run):
  input_file = run.model_inputs['out_dir'] + '/' + run.model_inputs['checkpoint_file'] + '.hdf5'
  
  print "Writing Run: " + run.title
  print "Input File: " + input_file
  print
  
  view = TimeView(input_file)

  # Times
  ts = view.get_ts() / pcs['spm']
  
  # Pressure at points
  if not realistic:
    pfos = view.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])
  else :
    # Coordinates of mesh vertices
    coord = view.mesh.coordinates()
    # x coords
    vx = coord[:,0]
    # y coords
    vy = coord[:,1]
    # Points to record pressure
    xs = array([15, 30, 60, 13.13]) * 1000.0 + vx.min()
    ys = array([10.4, 10.4, 10.4, 17.25]) * 1000.0 + vy.min()
    pfos = view.get_pfo_array_at_points(xs, ys)
  
  # Average pressure
  avg_pfos = view.get_avg_pfo_array()
  # Average melt
  avg_ms = view.get_avg_m_array()
  # Average sheet height
  avg_hs = view.get_avg_h_array()
  # Average sliding velocity 
  avg_ubs = view.get_avg_u_b_array()
  # Average conductivity
  avg_ks = view.get_avg_k_array()
  # Average englacial storage layer thickness
  #avg_hes = view.get_avg_h_e_array()
  
  out_dir = run.model_inputs['out_dir'] + '/txt_results/'
  
  if not os.path.exists(out_dir):
    os.makedirs(out_dir)
    
  savetxt(out_dir + 'ts.txt', ts)
  savetxt(out_dir + 'pfos.txt', pfos)
  savetxt(out_dir + 'avg_pfos.txt', avg_pfos)
  savetxt(out_dir + 'avg_ms.txt', avg_ms * pcs['spy'])
  savetxt(out_dir + 'avg_hs.txt', avg_hs)
  savetxt(out_dir + 'avg_ubs.txt', avg_ubs * pcs['spy'])
  savetxt(out_dir + 'avg_ks.txt', avg_ks)
  #savetxt(out_dir + 'avg_hes.txt', avg_hes)

print "Writing all runs."
# Otherwise write data for all runs
for run_title, run in experiment_db[experiment_title].winter_runs.iteritems():
  write_run(run)
