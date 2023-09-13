#! /usr/bin/env python

import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

si_phdisp = ppy.Phdisp.from_yaml('si_phdisp.yml')

# Create a figure and axis for plotting
fig, ax  = plt.subplots()

# Optional, used to format the plot
plt.rcParams.update(ppy.plot_tools.plotparams)

# Optional, used to label the q-points with labels for the FCC crystal structure.
# For example, [0.5, 0.5, 0.5] is the 'L' point in the FCC Brillouin zone.
si_phdisp.qpt.add_labels(ppy.lattice.points_fcc)

si_phdisp.plot_phdisp(ax)
plt.show()
#plt.savefig('phdisp.png')
