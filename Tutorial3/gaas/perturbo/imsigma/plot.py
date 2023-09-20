import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

# Example using the imsigma calculation mode
gaas_imsigma = ppy.Imsigma.from_yaml('gaas_imsigma.yml')


plt.rcParams.update(ppy.plot_tools.plotparams)
fig = plt.figure()
ax = fig.add_subplot(111)

#Bands 1 and 2
ax.scatter(gaas_imsigma.bands[1][:],gaas_imsigma.imsigma[1][1][:],color='b')


ax.set_xlabel('Energy(eV)')
ax.set_ylabel('ImSigma(meV)')
plt.savefig('gaas-imsigma.png')
