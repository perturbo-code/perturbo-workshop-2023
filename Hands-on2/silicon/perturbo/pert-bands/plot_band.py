#! /usr/bin/env python

import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
plt.rcParams.update(ppy.plot_tools.plotparams)

si_bands = ppy.Bands.from_yaml('si_bands.yml')
si_bands.kpt.add_labels(ppy.lattice.points_fcc)

si_bands.plot_bands(ax)
plt.show()
