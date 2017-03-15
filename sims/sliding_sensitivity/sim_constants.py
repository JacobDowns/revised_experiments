### Create a dictionary of physical constants

sim_constants = {}

# Seconds per day
sim_constants['spd'] = 60.0 * 60.0 * 24.0
# Seconds in a year
sim_constants['spy'] = 60.0 * 60.0 * 24.0 * 365.0              
# Seconds per month 
sim_constants['spm'] = sim_constants['spy'] / 12.0 
# Density of water (kg / m^3)
sim_constants['rho_w'] = 1000.0  
# Density of ice (kg / m^3)
sim_constants['rho_i'] = 910.0
# Gravitational acceleration (m / s^2)
sim_constants['g'] = 9.8 
# Flow rate factor of ice (1 / Pa^3 * s) 
sim_constants['A'] = 5e-25
# Average bump height (m)
sim_constants['h_r'] = 0.1
# Typical spacing between bumps (m)
sim_constants['l_r'] = 2.0      
# Sheet conductivity (m^(7/4) / kg^(1/2))
sim_constants['k'] = 5e-3
# Exponents 
sim_constants['alpha'] = 5. / 4.
sim_constants['beta'] = 3. / 2.
sim_constants['delta'] = sim_constants['beta'] - 2.0