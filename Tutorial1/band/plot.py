import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

fig, ax  = plt.subplots()

si_bands = ppy.Bands.from_yaml('pert_output.yml')

si_bands.plot_bands(ax)

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('si.bands')

plt.scatter(x[:,0],x[:,-1])

plt.show()
plt.savefig('band.png',dpi=400)
'''


