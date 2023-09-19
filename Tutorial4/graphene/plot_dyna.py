# This script plots electron population as a function of energy for input number of snapshots.
# graphene_popu.h5 and graphene_dynamics-pp.yml are required to be under the same directory as this script
import perturbopy.postproc as ppy 
import matplotlib.pyplot as plt
import numpy as np

# choose the indices of time snapshots to plot
plot_num = input("Enter number of snapshots to be plotted: ")
# check if inputs are reasonable
if not float(plot_num) == int(plot_num) or int(plot_num) < 1:
   raise ValueError('please input a positive integer for number of snapshots')

# set paths
popu_path = "graphene_popu.h5"
yaml_path = "graphene_dynamics-pp.yml"

# import post-processing data from yaml file
dyna_pp = ppy.DynaPP.from_hdf5_yaml(popu_path, yaml_path)

# extract postprocessing data from dyna_pp
time_vec = dyna_pp.times
time_unit = dyna_pp.time_units
energy_grid = dyna_pp.energy_grid
elec_popu = dyna_pp.popu

desired_time = np.linspace(time_vec[0], time_vec[-1], int(plot_num)) 
# find the nearest snapshots for the desired moments to plot
snap_vec = np.argmin(np.abs(time_vec[:, np.newaxis] - desired_time), axis=0)

# convert time to ps
if time_unit == 'fs':
   print('converting plot units to picoseconds')
   time_vec *= 0.0010
   new_time_unit = 'ps'
elif time_unit != 'ps':
   new_time_unit = time_unit
   print(f'plotting time in {time_unit}')

# initialize figures
fig, ax = plt.subplots(1, 1, figsize=(12,8))
plt.rcParams.update(ppy.plot_tools.plotparams)

# plot electron population as a function of energy for selected snapshots 
for snap_number in snap_vec:
    plt.plot(energy_grid, elec_popu[:, snap_number], linestyle='-', label=f't={time_vec[snap_number]:.2f} {new_time_unit}')

# set plot labels and legends
plt.legend()
plt.xlabel('Energy (eV)', fontsize=20)

plt.ylabel('Electron population', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig(f'graphene_dynamics.png')
plt.show()

