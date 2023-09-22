import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np


# Set path to files
cdyna_path = "gaas_cdyna.h5"
tet_path = "gaas_tet.h5"
dyna_run_yaml_path = "../dynamics-run/efield-0/gaas_dynamics-run.yml"
dyna_pp_yaml_path = "gaas_dynamics-pp.yml"

# Load dyna_run object
gaas_dyna_run = ppy.DynaRun.from_hdf5_yaml(cdyna_path, tet_path, dyna_run_yaml_path)

# Get steady state drift velocities
steady_drift_vel, _ = gaas_dyna_run.extract_steady_drift_vel(dyna_pp_yaml_path)
steady_drift_vel = np.asarray(steady_drift_vel)

# Set first value to zero for E=0
steady_drift_vel[0] = 0.0

# Create array of field strengths
efields = np.arange(0, 1601, 200)

# Rescale for plotting purposes
steady_drift_vel = np.asarray(steady_drift_vel) / 1e6

# Plot velocity-field curve
plt.rcParams.update(ppy.plot_tools.plotparams)
fig, ax = plt.subplots()

ax.plot((efields / 1000), steady_drift_vel, ls='', marker='o', markersize=5)

ax.set_xlabel('E (kV/cm)', fontsize=20)
ax.set_ylabel('$v_d$ ($10^6$ cm/s)', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig('velocity-field_curve.png')
# plt.show()
