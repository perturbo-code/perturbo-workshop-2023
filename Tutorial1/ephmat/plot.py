import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('si.ephmat')

plt.scatter(x[:,3],x[:,-2])

plt.show()
plt.savefig('band.jpg',dpi=400)



