import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
plt.rcParams.update(ppy.plot_tools.plotparams)

si_bands = ppy.Bands.from_yaml('si_bands.yml')
si_bands.kpt.add_labels(ppy.lattice.points_fcc)

si_bands.plot_bands(ax)
plt.savefig('band.jpg')

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('si.bands')

plt.scatter(x[:,0],x[:,-1])

plt.show()
plt.savefig('band.png',dpi=400)
'''


