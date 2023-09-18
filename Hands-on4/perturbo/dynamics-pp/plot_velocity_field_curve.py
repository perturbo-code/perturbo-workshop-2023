import yaml
import numpy as np
import matplotlib.pyplot as plt


# Parameters
prefix = 'gaas'
efields = np.arange(0, 1600, 200)
nsnaps_per_run = 20

# Store drift velocities at the end
# of each run
drift_vels = []

# yml file
yml_file = f'{prefix}_dynamics-pp.yml'

# Opening yml file
with open(yml_file, 'r') as stream:
    try:
        # Converts yaml document to python object
        dct = yaml.safe_load(stream)

    except yaml.YAMLError as e:
        print(e)

# Get velocities from dictionary
vels_efield = dct['dynamics-pp']['velocity']

# Loop over field strengths
for i, efield in enumerate(efields):
    if i == 0:
        # Hard code to 0 as not outputted
        # when E = 0
        vel_i = 0.0
    else:
        # Get drift velocity of final snap in run
        idx = i * nsnaps_per_run + (nsnaps_per_run - 1)
        vel_i = (-1.0) * vels_efield[idx]

    # Store in list
    drift_vels.append(vel_i)

# Rescale for plotting purposes
drift_vels = np.asarray(drift_vels) / 1e6

# Plot velocity-field curve
fig, ax = plt.subplots()
ax.plot((efields / 1000), drift_vels, ls='', marker='o')
ax.set_xlabel('E (kV/cm)')
ax.set_ylabel('$v_d$ ($10^6$ cm/s)')
plt.savefig('velocity-field_curve.png')
# plt.show()
