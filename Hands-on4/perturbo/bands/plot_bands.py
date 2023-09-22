import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.rcParams.update(ppy.plot_tools.plotparams)

gaas_bands = ppy.Bands.from_yaml('gaas_bands.yml')
gaas_bands.kpt.add_labels(ppy.lattice.points_fcc)

# Plot band diagram
gaas_bands.plot_bands(ax)

plt.savefig('gaas_bands.png')
# plt.show()

# Plot zoomed in band diagram
fig, ax2 = plt.subplots()

gaas_bands.plot_bands(ax2, energy_window=[5, 8])

plt.savefig('gaas_bands_zoom.png')
# plt.show()
