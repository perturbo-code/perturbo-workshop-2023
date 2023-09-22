import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np


# Set path to files
popu_path = "gaas_popu.h5"
dyna_pp_yaml_path = "gaas_dynamics-pp.yml"

# Load dyna_pp object
gaas_dyna_pp = ppy.DynaPP.from_hdf5_yaml(popu_path, dyna_pp_yaml_path)

# Plot figure
plt.rcParams.update(ppy.plot_tools.plotparams)
fig, ax = plt.subplots()

# Plot end point for each run
snap_numbers = np.arange(19, 180, 20)

for snap_number in snap_numbers:
    plt.plot(
            gaas_dyna_pp.energy_grid,
            gaas_dyna_pp.popu[:, snap_number],
            marker='o',
            linestyle='',
            markersize=2.5)

plt.xlabel('Energy (eV)', fontsize=20)
plt.ylabel('Electron population', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig('occupations.png')
# plt.show()
