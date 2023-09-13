import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

# Example using the imsigma calculation mode
si_imsigma = ppy.Imsigma.from_yaml('si_imsigma.yml')


plt.rcParams.update(ppy.plot_tools.plotparams)
fig = plt.figure()
ax = fig.add_subplot(111)

#Bands 1 and 2
ax.scatter(si_imsigma.bands[1][:],si_imsigma.imsigma[1][1][:],color='b')
ax.scatter(si_imsigma.bands[2][:],si_imsigma.imsigma[1][2][:],color='b')

ax.set_xlim(6.63,6.9)
ax.set_ylim(0.,15.)
ax.set_xlabel('Energy(eV)')
ax.set_ylabel('ImSigma(meV)')
plt.savefig('si-imsigma.png')



