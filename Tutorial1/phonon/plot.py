import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('si.phdisp')

plt.scatter(x[:,0],x[:,-1])

plt.show()
plt.savefig('band.jpg',dpi=400)



