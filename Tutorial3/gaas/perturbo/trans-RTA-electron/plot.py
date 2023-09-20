import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

gaas_trans_rta = ppy.Trans.from_yaml('gaas_trans-rta.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

temperatures = np.array(list(gaas_trans_rta.temper.values()))

# Get xx components of mobilities
mobilities = np.array(list(gaas_trans_rta.mob.values()))[:, 0, 0]

ax.plot(temperatures, mobilities,marker='o')

ax.set_xlabel(f"Temperature ({gaas_trans_rta.temper.units})")
ax.set_ylabel(f"Mobility ({gaas_trans_rta.mob.units})")

plt.title('Mobility vs Temperature - GaAs')
plt.show()
plt.savefig('gaas-trans-rta.png')
