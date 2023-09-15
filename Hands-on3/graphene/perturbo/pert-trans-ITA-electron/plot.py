import perturbopy.postproc as ppy
import matplotlib.pyplot as plt
import numpy as np

graphene_trans_ita = ppy.Trans.from_yaml('graphene_trans-ita.yml')

fig, ax  = plt.subplots()

# Optional
plt.rcParams.update(ppy.plot_tools.plotparams)

temperatures = np.array(list(graphene_trans_ita.temper.values()))

# Get xx components of mobilities
mobilities = np.array(list(graphene_trans_ita.mob.values()))[:, 0, 0]

ax.plot(temperatures, mobilities,marker='o')

ax.set_xlabel(f"Temperature ({graphene_trans_ita.temper.units})")
ax.set_ylabel(f"Mobility ({graphene_trans_ita.mob.units})")

plt.show()
plt.savefig('graphene-trans-ita.png')



