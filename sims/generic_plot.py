from pylab import *
from txt_results_reader import *

experiment_title = sys.argv[1]
reader = TxtResultsReader(experiment_title)
matplotlib.rcParams.update({'font.size': 16})
lw = 2.5
N = len(reader.run_titles)


### Test point pressures

fig = figure(figsize = (13., 13))

for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]

  subplot(N, 1, i + 1)
  title(run_title + ' PFO')
  
  for j in range(len(reader.pfos[i])):
    plot(reader.ts, reader.pfos[i][j,:], linewidth = lw, label = str(j))
  
  xlim([0.0, max(reader.ts)])
  xlabel('Time (Months)')
  ylabel('Water Pressure (Flotation Fraction)')
  legend()
  grid(True)
  
savefig(experiment_title + '/plot/images/pfos.png', dpi = 500)  
  
  
  
### Plot Average Pressure

fig = figure(figsize = (13., 5.5))

title(experiment_title + ' Avg. PFO')
for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]
  plot(reader.ts, reader.avg_pfos[i], linewidth = lw, label = run_title)
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('Water Pressure (Flotation Fraction)')
legend()
grid(True)
savefig(experiment_title + '/plot/images/avg_pfos.png', dpi = 500)



### Plot Average sheet height

fig = figure(figsize = (13., 5.5))

title(experiment_title + ' Avg. Sheet Height')
for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]
  plot(reader.ts, reader.avg_hs[i], linewidth = lw, label = run_title)
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('Sheet Height (m)')
legend()
grid(True)
savefig(experiment_title + '/plot/images/avg_hs.png', dpi = 500)



### Plot average melt input

fig = figure(figsize = (13., 5.5))

title(experiment_title + ' Avg. Melt')
for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]
  plot(reader.ts, reader.avg_ms[i], linewidth = lw, label = run_title)
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('Melt (m/a)')
legend()
grid(True)
savefig(experiment_title + '/plot/images/avg_ms.png', dpi = 500)



### Plot average sliding speed

fig = figure(figsize = (13., 5.5))

title(experiment_title + ' Avg. Sliding Speed')
for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]
  plot(reader.ts, reader.avg_ubs[i], linewidth = lw, label = run_title)
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('Sliding Speed (m/a)')
legend()
grid(True)
savefig(experiment_title + '/plot/images/avg_ubs.png', dpi = 500)



### Plot average conductivity

fig = figure(figsize = (13., 5.5))

title(experiment_title + ' Avg. Conductivity')
for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]
  plot(reader.ts, reader.avg_ks[i], linewidth = lw, label = run_title)
  
xlim([0.0, max(reader.ts)])
xlabel('Time (Months)')
ylabel('k')
legend()
grid(True)
savefig(experiment_title + '/plot/images/avg_ks.png', dpi = 500)