#! /usr/bin/env python

import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

si_ephmat = ppy.Ephmat.from_yaml('si_ephmat.yml')

plt.rcParams.update(ppy.plot_tools.plotparams)
si_ephmat.qpt.add_labels(ppy.lattice.points_fcc)

fig1, ax1  = plt.subplots()
si_ephmat.plot_ephmat(ax1)
#plt.show()
plt.savefig('si_ephmat.png')


fig2, ax2  = plt.subplots()
si_ephmat.plot_defpot(ax2)
plt.savefig('si_defpot.png')
#plt.show()

fig3, ax3  = plt.subplots()
si_ephmat.plot_phdisp(ax3)
plt.savefig('si_phdisp.png')
