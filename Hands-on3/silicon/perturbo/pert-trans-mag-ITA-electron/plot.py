import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

si_trans_rta = ppy.Trans.from_yaml('../pert-trans-mag-RTA-electron/si_trans-mag-rta.yml')
si_trans_ita = ppy.Trans.from_yaml('si_trans-mag-ita.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

#z component of magnetic field
bfield_rta = np.array(list(si_trans_rta.bfield.values()))[:,2]
bfield_ita = np.array(list(si_trans_ita.bfield.values()))[:,2]

# Get xy components of conductivities
conductivities_rta = np.array(list(si_trans_rta.cond.values()))[:, 0, 1]
conductivities_ita = np.array(list(si_trans_ita.cond.values()))[:, 0, 1]

ax.plot(bfield_rta, conductivities_rta,marker='o',color='b',label='mag-RTA')
ax.plot(bfield_ita, conductivities_ita,marker='o',color='r',label='mag-ITA')


ax.set_xlabel(f"Magnetic field ({si_trans_rta.bfield.units})")
ax.set_ylabel(f"Conductivity ({si_trans_rta.cond.units})")
ax.legend(fontsize=14)
plt.savefig('si-trans-mag.png')
