#! /usr/bin/env python

import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

gaas_ephmat = ppy.Ephmat.from_yaml('gaas_ephmat.yml')

plt.rcParams.update(ppy.plot_tools.plotparams)
gaas_ephmat.qpt.add_labels(ppy.lattice.points_fcc)

fig1, ax1  = plt.subplots()
gaas_ephmat.plot_ephmat(ax1,log=True)
#plt.show()
plt.savefig('gaas_ephmat.png')

fig3, ax3  = plt.subplots()
gaas_ephmat.plot_phdisp(ax3)
plt.savefig('gaas_ephmat_phdisp.png')
