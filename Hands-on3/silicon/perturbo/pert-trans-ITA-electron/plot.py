import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

si_trans_ita = ppy.Trans.from_yaml('si_trans-ita.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

temperatures = np.array(list(si_trans_ita.temper.values()))

# Get xx components of mobilities
mobilities = np.array(list(si_trans_ita.mob.values()))[:, 0, 0]

ax.plot(temperatures, mobilities,marker='o')

ax.set_xlabel(f"Temperature ({si_trans_ita.temper.units})")
ax.set_ylabel(f"Mobility ({si_trans_ita.mob.units})")

plt.show()
plt.savefig('si-trans-ita.png')



