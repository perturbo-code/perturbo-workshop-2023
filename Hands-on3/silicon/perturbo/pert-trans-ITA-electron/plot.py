import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

si_trans_rta = ppy.Trans.from_yaml('../pert-trans-RTA-electron/si_trans-rta.yml')
si_trans_ita = ppy.Trans.from_yaml('si_trans-ita.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

temperatures_rta = np.array(list(si_trans_rta.temper.values()))
temperatures_ita = np.array(list(si_trans_ita.temper.values()))

# Get xx components of mobilities
mobilities_rta = np.array(list(si_trans_rta.mob.values()))[:, 0, 0]
mobilities_ita = np.array(list(si_trans_ita.mob.values()))[:, 0, 0]

ax.plot(temperatures_rta, mobilities_rta,marker='o',color='b',label='RTA')
ax.plot(temperatures_ita, mobilities_ita,marker='o',color='r',label='ITA')


ax.set_xlabel(f"Temperature ({si_trans_rta.temper.units})")
ax.set_ylabel(f"Mobility ({si_trans_rta.mob.units})")
ax.legend(fontsize=14)
plt.savefig('si-trans.png')
