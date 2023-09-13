import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

si_trans_mag_ita = ppy.Trans.from_yaml('si_trans-mag-ita.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

bfield = np.array(list(si_trans_mag_ita.bfield.values()))[:,2]

# Get xx components of conductivities
conductivities = np.array(list(si_trans_mag_ita.cond.values()))[:, 0, 1]
print(bfield,conductivities)
ax.plot(bfield, conductivities,marker='o')

ax.set_xlabel(f"B-field ({si_trans_mag_ita.bfield.units})")
ax.set_ylabel(f"Hall conductivity ({si_trans_mag_ita.cond.units})")

plt.show()
plt.savefig('si-trans-mag-ita.png')

