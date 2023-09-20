import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

gaas_bands = ppy.Bands.from_yaml('gaas_bands.yml')

fig, ax  = plt.subplots()

# Setting plot parameter stuffs
ppy.plot_tools.plotparams["lines.linewidth"] = 2.0
plt.rcParams.update(ppy.plot_tools.plotparams)

gaas_bands = ppy.Bands.from_yaml('gaas_bands.yml')
gaas_bands.kpt.add_labels(ppy.lattice.points_fcc)

gaas_bands.plot_bands(ax)
ax.fill_between((0,3.7802390), 5.665, 6.265, color='yellow')
ax.axhline(y=5.665, color='lightgrey', linestyle='--')
ax.axhline(y=6.265, color='lightgrey', linestyle='--')

plt.title('GaAs - bands')
plt.savefig('gaas-bands.png')
plt.show()
