import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

# Example using the imsigma calculation mode
graphene_imsigma = ppy.Imsigma.from_yaml('graphene_imsigma.yml')


plt.rcParams.update(ppy.plot_tools.plotparams)
fig = plt.figure()
ax = fig.add_subplot(111)

#Bands 1 
ax.scatter(graphene_imsigma.bands[1][:],graphene_imsigma.imsigma[1][1][:],color='b')

ax.set_xlabel('Energy(eV)')
ax.set_ylabel('ImSigma(meV)')
plt.savefig('graphene-imsigma.png')



