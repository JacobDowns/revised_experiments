from txt_results_reader import *
import sys

### Computes SPV ratios for an experiment

experiment_title = sys.argv[1]
reader = TxtResultsReader(experiment_title)
N = len(reader.run_titles)
indexes = reader.ts > 1.0

print "SPV Ratios"
print

min_max = {}
min_max['0'] = []
min_max['1'] = []
min_max['2'] = []
min_max['3'] = []
min_max['d'] = []

for i in range(len(reader.run_titles)):
  run_title = reader.run_titles[i]
  print run_title
  print

  ### Compute SPV ratios at test points
  for j in range(len(reader.pfos[i])):
    # Compute SPV ratio at this point
    spv = average(reader.pfos[i][j,:][indexes]) / reader.pfos[i][j,:][0]
  
    print "Point " + str(j) + " : " + str(spv)
    print    
    
    min_max[str(j)].append(spv)
    
    
  ### Compute whole domain SPV ratio
  spvd = average(reader.avg_pfos[i][indexes]) / reader.avg_pfos[i][0] 
  print "SPVD: " + str(spvd)    
  print
  
  min_max['d'].append(spvd)

print
print "SPV1 Min: " + str(min(min_max['0']))
print "SPV1 Max: " + str(max(min_max['0']))
print
print "SPV2 Min: " + str(min(min_max['1']))
print "SPV2 Max: " + str(max(min_max['1']))
print
print "SPV3 Min: " + str(min(min_max['2']))
print "SPV3 Max: " + str(max(min_max['2']))
print
print "SPVD Min: " + str(min(min_max['d']))
print "SPVD Max: " + str(max(min_max['d']))
print
print "SPV4 Min: " + str(min(min_max['3']))
print "SPV4 Max: " + str(max(min_max['3']))
print

  

    
  

