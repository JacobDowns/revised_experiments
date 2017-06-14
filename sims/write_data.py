from dolfin import *
from time_view import *
from pylab import *
from sim_constants import *
from experiment_db import *
import sys

"""
Write data to text files for plotting -- speeds things up when lots of plot 
tweaks are needed. 
"""

# Process number
MPI_rank = MPI.rank(mpi_comm_world())
experiment_title = sys.argv[1]

run_title = None
if len(sys.argv) > 2:
  run_title = sys.argv[2]

run = experiment_db[experiment_title].runs[run_title]

def write_run(run):
  print "Writing..."
  print "Experiment: " + experiment_title
  print "Run: " + run_title
  print
  
  input_file = run.model_inputs['out_dir'] + '/' + run.model_inputs['checkpoint_file'] + '.hdf5'
  view = TimeView('../hdf5_results/' + labels[i] + '.hdf5')
  
  # Times
  ts = view.get_ts() / pcs['spm']
  # Pressure at points
  pfos = view.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])
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
  
  out_dir = run.model_inputs['out_dir'] + '/txt_results/'
  savetxt(out_dir + 'ts.txt', ts)
  savetxt(out_dir + 'pfos' + str(i) + '.txt', pfos)
  savetxt(out_dir + 'avg_pfos' + str(i) + '.txt', avg_pfos)
  savetxt(out_dir + 'avg_ms' + str(i) + '.txt', avg_ms * pcs['spy'])
  savetxt(out_dir + 'avg_hs' + str(i) + '.txt', avg_hs)
  savetxt(out_dir + 'avg_ubs' + str(i) + '.txt', avg_ubs * pcs['spy'])
  savetxt(out_dir + 'avg_ks' + str(i) + '.txt', avg_ks)
  
  
write_run(run)

### If a run title is specified, write data for that run alone
#if run_title :

  

  

"""

### Get data

labels = ['low_one', 'low_two', 'low_week', 'high_one', 'high_two', 'high_week']


for i in range(len(labels)):
  print i 
  label = labels[i]
  view = TimeView('../hdf5_results/' + labels[i] + '.hdf5')

  # Times
  ts = view.get_ts() / pcs['spm']
  # Pressure at points
  pfos = view.get_pfo_array_at_points([10e3, 20e3, 50e3], [10e3, 10e3, 10e3])
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
  
  savetxt('ts.txt', ts)
  savetxt('pfos' + str(i) + '.txt', pfos)
  savetxt('avg_pfos' + str(i) + '.txt', avg_pfos)
  savetxt('avg_ms' + str(i) + '.txt', avg_ms * pcs['spy'])
  savetxt('avg_hs' + str(i) + '.txt', avg_hs)
  savetxt('avg_ubs' + str(i) + '.txt', avg_ubs * pcs['spy'])
  savetxt('avg_ks' + str(i) + '.txt', avg_ks)
  

view = TimeView('../hdf5_results/high_month.hdf5')
ts = view.get_ts() / pcs['spm']
out1 = File('pvds/pfo.pvd')
out2 = File('pvds/h.pvd')
out3 = File('pvds/m.pvd')
out4 = File('pvds/u_b.pvd')

for i in range(0, len(ts), 2):
  print i
  out1 << view.get_pfo(i)
  out2 << view.get_h(i)
  out3 << view.get_m(i)
  out4 << view.get_u_b(i)"""
