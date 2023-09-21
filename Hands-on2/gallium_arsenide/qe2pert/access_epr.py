import h5py
import numpy as np

f = h5py.File('gaas_epr.h5', 'r')
f_key = list(f.keys())
print('f_key_list=',f_key)

#basic_data
print('\n\n',10*'-'+'basic_data'+10*'-')
basic_data = f['basic_data']
print('type of basic_data:',type(basic_data))

basic_data_key = list(basic_data.keys())
print('keys of basic_data:', basic_data_key)

print('basic_data.alat',np.array(basic_data[basic_data_key[0]]))

for ikey in basic_data_key:
    print(str(ikey),np.array(basic_data[ikey]))


#electron_wannier
print('\n\n',10*'-'+'electron_wannier'+10*'-')
electron_wannier = f['electron_wannier']
print('type of electron_wannier:',type(electron_wannier))

electron_wannier_key = list(electron_wannier.keys())
print('keys of electron_wannier :', electron_wannier_key)

for ikey in electron_wannier_key:
    print('electron_wannier.shape',np.array(electron_wannier[ikey]).shape)


#eph_matrix_wannier
print('\n\n',10*'-'+'eph_matrix_wannier'+10*'-')
eph_matrix_wannier = f['eph_matrix_wannier']
print('type of eph_matrix_wannier:',type(eph_matrix_wannier))

eph_matrix_wannier_key = list(eph_matrix_wannier.keys())
print('keys of eph_matrix_wannier :', eph_matrix_wannier_key)

for ikey in eph_matrix_wannier_key:
    print('eph_matrix_wannier.shape',np.array(eph_matrix_wannier[ikey]).shape)


#force_constant
print('\n\n',10*'-'+'force_constant'+10*'-')
force_constant = f['force_constant']
print('type of force_constant:',type(force_constant))

force_constant_key = list(force_constant.keys())
print('keys of force_constant :', force_constant_key)

for ikey in force_constant_key:
    print('force_constant.shape',np.array(force_constant[ikey]).shape)


f.close()
