import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

si_trans_ita = ppy.Trans.from_yaml('../pert-trans-ITA-electron/si_trans-ita.yml')
si_trans_ita_phexclude = ppy.Trans.from_yaml('si_trans-ita.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

temperatures_ita = np.array(list(si_trans_ita.temper.values()))
temperatures_ita_phexclude = np.array(list(si_trans_ita_phexclude.temper.values()))

# Get xx components of mobilities
mobilities_ita = np.array(list(si_trans_ita.mob.values()))[:, 0, 0]
mobilities_ita_phexclude = np.array(list(si_trans_ita_phexclude.mob.values()))[:, 0, 0]

ax.plot(temperatures_ita, mobilities_ita,marker='o',color='b',label='ITA')
ax.plot(temperatures_ita_phexclude, mobilities_ita_phexclude,marker='o',color='r',label='ITA-ph-exclude-1,2')


ax.set_xlabel(f"Temperature ({si_trans_ita.temper.units})")
ax.set_ylabel(f"Mobility ({si_trans_ita.mob.units})")
ax.legend(fontsize=14)
plt.savefig('si-trans-phexclude.png')
