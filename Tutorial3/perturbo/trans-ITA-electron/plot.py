import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

gaas_trans_ita = ppy.Trans.from_yaml('gaas_trans-ita.yml')
gaas_trans_rta = ppy.Trans.from_yaml('../trans-RTA-electron/gaas_trans-rta.yml')
fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

temperatures = np.array(list(gaas_trans_ita.temper.values()))

# Get xx components of mobilities
mobilities_ita = np.array(list(gaas_trans_ita.mob.values()))[:, 0, 0]
mobilities_rta = np.array(list(gaas_trans_rta.mob.values()))[:, 0, 0]

ax.plot(temperatures, mobilities_ita,marker='o',label='ITA')
ax.plot(temperatures, mobilities_rta,marker='o',label='RTA')

ax.set_xlabel(f"Temperature ({gaas_trans_ita.temper.units})")
ax.set_ylabel(f"Mobility ({gaas_trans_ita.mob.units})")

plt.title('Mobility vs Temperature - GaAs')
plt.show()
plt.legend()
plt.savefig('gaas-trans.png')
