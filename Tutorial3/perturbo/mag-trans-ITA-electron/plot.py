import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

gaas_trans_mag_ita = ppy.Trans.from_yaml('gaas_trans-mag-ita.yml')
gaas_trans_mag_rta = ppy.Trans.from_yaml('../mag-trans-RTA-electron/gaas_trans-mag-rta.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

bfield = np.array(list(gaas_trans_mag_ita.bfield.values()))[:,2]

# Get xx components of conductivities
conductivities_ita = np.array(list(gaas_trans_mag_ita.cond.values()))[:, 0, 1]
conductivities_rta = np.array(list(gaas_trans_mag_rta.cond.values()))[:, 0, 1]

ax.plot(bfield, conductivities_ita,marker='o',label='ITA')
ax.plot(bfield, conductivities_rta,marker='o',label='RTA')

ax.set_xlabel(f"B-field ({gaas_trans_mag_ita.bfield.units})")
ax.set_ylabel(f"Hall conductivity ({gaas_trans_mag_ita.cond.units})")

plt.legend()
plt.title('Hall conductivity vs magnetic field')
plt.show()
plt.savefig('gaas-trans-mag-ita-vs-rta.png')
