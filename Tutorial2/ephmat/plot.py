import perturbopy.postproc as ppy

si_ephmat = ppy.Ephmat.from_yaml('si_ephmat.yml')

import matplotlib.pyplot as plt

plt.rcParams.update(ppy.plot_tools.plotparams)
si_ephmat.qpt.add_labels(ppy.lattice.points_fcc)

fig, ax  = plt.subplots()
si_ephmat.plot_ephmat(ax)
plt.show()

plt.savefig('ephmat.jpg',dpi=400)



