# Hands-On 4: Velocity-Field Curves in GaAs

In this tutorial we will learn about the ultrafast dynamics calculations in Perturbo by determining the velocity-field curve in GaAs. 

Velocity-field curves describe the mean drift velocity of the charge carriers in a material with an applied electric field. The drift velocity typically increases linearly at low fields, with a slope equal to the carrier mobility, and then saturates at high fields. Detailed knowledge of the mechanisms governing the mobility and the saturation velocity is important to advance electronic devices. 

The equation for the drift velocity is 

![Equation for drift velocity](https://github.com/perturbo-code/perturbo-workshop-2023/blob/main/Hands-on4/images/drift_velocity_eq.png)

In a recent paper[1](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.L100303), the velocity-field curve was calculated for Si, GaAs and graphene both in low and high fields. In this tutorial we will attempt to replicate the curve for GaAs with smaller sampling and less convergence due to time constraints. 

![Drift velocity curves from paper](https://github.com/perturbo-code/perturbo-workshop-2023/blob/main/Hands-on4/images/velocity_field_curve.png)

## 0. Setup

### git pull

Do a git pull to make sure the repo is up to date 

```
cd perturbo-workshop-2023
git pull
```

### Download and install perturbopy

```
git clone https://github.com/perturbo-code/perturbopy.git
pip install .
```

For more information about perturbopy, click here [perturbopy](https://perturbopy.readthedocs.io/en/latest/index.html)

### Get epr file

NB!!!!!! GET gaas\_epr.h5 FILE


### Create docker

Click here, [docker for Perturbo](https://perturbo-code.github.io/mydoc_docker.html) for more information on how to download and install docker, and how to pull the docker image you require

Run the docker by using one of the following commands

for ifort version:

```
docker run -v <location of github repo>/perturbo-workshop-2023:/home/user/run/perturbo-workshop-2023 --user 500 -it --rm --name perturbo-workshop perturbo/perturbo:ifort
```

for gcc version:
```
docker run -v <location of github repo>/perturbo-workshop-2023:/home/user/run/perturbo-workshop-2023 --user 500 -it --rm --name perturbo-workshop perturbo/perturbo:gcc
```

## 1. Bands

First we want to calculate the band structure of GaAs. This will help us determine where to set the energy minimum and maximum for the dynamics calculations. 

Start by moving into the bands directory

```
cd perturbo-workshop-2023/Hands-on4/perturbo/bands/
```

### Input files

The input files for *calc_mode=bands* are

pert.in:

```
&perturbo
 prefix      = 'gaas'          
 calc_mode   = 'bands'         
 fklist   = 'gaas_band.kpt'    
/
```

gaas\_band.kpt: 

```
6
  0.500 0.500 0.500  50 !L
  0.000 0.000 0.000  50 !G
  0.500 0.000 0.500  20 !X 
  0.500 0.250 0.750  20 !W
  0.375 0.375 0.750  50 !K
  0.000 0.000 0.000  1  !G
```

The kpt file gives the list of high-symmetry k points to plot the bands along. The first line specifies how many lines there are below the first line. Columns 1-3 give, respectively, the x, y, and z coordinates of a crystal momentum in crystal coordinates. The last column is the number of points from the current crystal momentum to the next crystal momentum.

### Running perturbo.x

We will now run Perturbo. In order to do so we must first link the epr file to the current directory

```
ln -sf ../../qe2pert/gaas_epr.h5
```

We can then run perturbo.x

```
perturbo.x -i pert.in > pert.out
```

### Output

*calc_mode=bands* gives the following output files
- YAML file, called pert\_output.yml, containing the inputs and outputs of the bands calculation.
- gaas.bands contains the information unique to the bands calculation, including the interpolated band structure. 

### Plotting bands

We can now plot the bands using perturbopy outside the docker using the python file plot\_bands.py

```
import perturbopy.postproc as ppy
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.rcParams.update(ppy.plot_tools.plotparams)

gaas_bands = ppy.Bands.from_yaml('gaas_bands.yml')
gaas_bands.kpt.add_labels(ppy.lattice.points_fcc)

# Plot band diagram
gaas_bands.plot_bands(ax)

plt.savefig('gaas_bands.png')
# plt.show()

# Plot zoomed in band diagram
fig, ax2 = plt.subplots()

gaas_bands.plot_bands(ax2, energy_window=[5, 7])

plt.savefig('gaas_bands_zoom.png')
# plt.show()
```

This simple script uses perturbopy. It is run by the simple command below

```
python plot_bands.py
```

This will create two files:
- gaas_bands.png: Displays band structure of GaAs
- gaas_bands_zoom.png: Displays zoomed in version of band structure of GaAs

![gaas_band](https://github.com/perturbo-code/perturbo-workshop-2023/blob/main/Hands-on4/images/computation_schematic.png)

![gaas_band_zoomed](https://github.com/perturbo-code/perturbo-workshop-2023/blob/main/Hands-on4/images/computation_schematic.png)

## 2. Setup Calculation

Before we can run the dynamics calculations, we need to run *calc_mode=setup*. Move into the setup directory

```
cd ../setup
```

### Input files

The input files for *calc_mode=setup* are

pert.in:

```
&perturbo
  prefix      = 'gaas'
  calc_mode   = 'setup'

  boltz_kdim(1)       = 60
  boltz_kdim(2)       = 60
  boltz_kdim(3)       = 60
  boltz_emin          = 5.665  !CBM=6.065
  boltz_emax          = 6.365  
  band_min            = 5
  band_max            = 5
  ftemper             = 'gaas.temper'
  hole                = .false.
 /
``` 

*boltz_kdim* gives the sampling of k points in each of the 3 directions. *boltz_emin* and *boltz_emax* give the minimum and maximum of the energy window. This is important as it reduced the number of scattering channels we need to calculate for. Here, it is set to be around the conduction band minima????? Similarly, *band_min* and *band_max* refers to the band numbers included in the calculation. *hole* is set to *.true.* if we are calculating for holes as opposed to electrons. Finally, *ftemper* is the temperature file. 

gaas.temper:

```
    1     F
  300.00          6.0425595703           0.9855601E+17
```

In the case of ultrafast dynamics calculations, the only number that is used here is the temperature since this will give the distribution of the phonons. The distribution of carriers is set in the dynamics-run input file.

Note, with more time, it would be useful to increase the *boltz_kdim* and *boltz_emax* parameters.

### Running perturbo.x

Before running the calculation, make a symbolic link to the epr file

```
ln -sf ../../qe2pert/gaas_epr.h5
```

We can then run the calculation with the following command

```
perturbo.x -i pert.in > pert.out
```

### Output

The output file we're interested in for ultrafast dynamics is the gaas\_tet.h5 file. It contains information on the k points (both in the irreducible wedge and full grid) and the associated k point tetrahedra in the energy window of interest. 


## 3. Dynamics-run

The next step is to run the time stepping of the Boltzmann transport equation (BTE) which will provide us with the electron distribution, f<sub>nk</sub> (t), that we'll need to determine the drift velocities. We need to find these for different electric field strengths and we need to let the calculation run to convergence in order to get at the steady state values of the drift velocity. 

This is done by starting with zero applied field and letting the calculation run to convergence. We then need to increase the electric field strength in steps, each time restarting the calculation from the previous, converged distribution and letting it run to convergence. This procedure is shown in the schematic below

![Schematic showing how the distribution is extracted at each electric field strength](https://github.com/perturbo-code/perturbo-workshop-2023/blob/main/Hands-on4/images/computation_schematic.png)

The distribution used for calculating the drift velocity is the final value of f<sub>nk</sub> (t) upon convergence. 

We will now go about performing the calculation of f<sub>nk<\sub> by running *calc_mode=dynamics-run*. First we must change to the dynamics-run directory
```
cd ../dynamics-run
```

### Input

Since we are running the calculation for multiple electric field strengths, we have the following script 

run.sh

```
#!/bin/bash

PREFIX='gaas'

# Test with two values first, then run full selection
# EFIELDS=($(seq 200 200 400))
# EFIELDS=($(seq 200 200 3000))
# EFIELDS=(0)
EFIELDS=($(seq 0 200 3000))

# OpenMP variables
OMP_THREADS=4

# Commands change slightly based on OS
# OS='MACOS'
OS='LINUX'

for efield in ${EFIELDS[@]}
do
   echo dynamics-run for Efield= $efield

   DIR=efield-$efield
   mkdir -p $DIR

   cd $DIR

   #change pert.in
   cp ../pert-ref.in  ./pert.in
   if [ "$OS" == "MACOS" ]; then
      sed -i '' "s|.*boltz_efield(1).*| boltz_efield(1)      = $efield.0|g"   pert.in
      if [ $efield != 0 ]; then
         sed -i '' "s|.*boltz_init_dist.*| boltz_init_dist      = 'restart'|g"   pert.in
         sed -i '' "s|.*load_scatter_eph.*| load_scatter_eph      = .true.|g"   pert.in
      fi
   elif [ "$OS" == "LINUX" ]; then
      sed -i "s|.*boltz_efield(1).*| boltz_efield(1)      = $efield.0|g"   pert.in

      if [ $efield != 0 ]; then
         sed -i "s|.*boltz_init_dist.*| boltz_init_dist      = 'restart'|g"   pert.in
         sed -i "s|.*load_scatter_eph.*| load_scatter_eph      = .true.|g"   pert.in
      fi
   else
      echo OS not supported
   fi

   # link prefix_epr.h5 and prefix_tet.h5
      ln -sf ../../../qe2pert/${PREFIX}_epr.h5
      ln -sf ../../setup/${PREFIX}_tet.h5

   # copy prefix.temper
   cp ../../setup/${PREFIX}.temper .

   # If restarting, need to link cdyna file
   # and tmp directory
   if [ $efield != 0 ]; then
      echo Linking cdyna and tmp
      ln -sf ../efield-0/${PREFIX}_cdyna.h5
      ln -sf ../efield-0/tmp
   fi

   # run pertubo.x
   export OMP_NUM_THREADS=${OMP_THREADS}
   perturbo.x -i pert.in > pert.out

   echo Done $efield

   # wait for a short period of time.  
   #done, return to upper directory.   
   cd ..

   sleep 1
done
```

This will create a efield-{efield value} folder for each electric field strength. 

We also have the pert-ref.in file which will become the pert.in file for each electric field strength.  
pert-ref.in

```
&perturbo
 prefix               = 'gaas'
 calc_mode            = 'dynamics-run'
 boltz_kdim(1)        = 60
 boltz_kdim(2)        = 60
 boltz_kdim(3)        = 60
 boltz_qdim(1)        = 10
 boltz_qdim(2)        = 10
 boltz_qdim(3)        = 10
 boltz_efield(1)      = 0.0
 boltz_efield(2)      = 0.0
 boltz_efield(3)      = 0.0
 boltz_emin           = 5.665
 boltz_emax           = 6.465
 band_min             = 5
 band_max             = 5
 hole                 = .false.
 ftemper              = 'gaas.temper'
 time_step            = 20.0
 boltz_nstep          = 100
 output_nstep         = 5
 boltz_init_dist      = 'fermi'
 boltz_init_smear     = 25.865213999999998
 boltz_init_e0        = 6.0344
 load_scatter_eph     = .false.
 tmp_dir              = './tmp'
 boltz_norm_dist      = .true.
 solver               = 'euler'
 ! boltz_acc_thr        = 1.0
/
```

The parameters that are commented out lets the calculation come to an end when it is converged. However, these are not yet in the public version of Perturbo

### Running perturbo.x

We run the bash script which also takes care of linking the epr and tet files, as well as copying the temper file

```
chmod +x run.sh
./run.sh
```

### Output

The two output files from the *dynamics-run* calculation are *gaas\_cdyna.h5* and *gaas_dynamics-run.yml*. However, all calculations will use the same cdyna file so the actual cdyna file is contained in *efield-0* folder and has a number of runs equal to the number of electric field strengths we calculate for. 

## 4. dynamics-pp

The final Perturbo calculation that must be run is *calc_mode=dynamics-pp*. This will give the average distribution as a function of energy and time, as well as the drift velocity. 

Move to the dynamics-pp folder

```
cd ../dynamics-pp
```

### Input files

run.sh

```
#!/bin/bash

PREFIX='gaas'

# Test with two values first, then run full selection
# EFIELDS=($(seq 200 200 3000))
EFIELDS=(0)
# EFIELDS=($(seq 0 200 3000))
 
# OpenMP variables
OMP_THREADS=4

OS='LINUX'

for efield in ${EFIELDS[@]}
do
   echo dynamics-pp for Efield= $efield

   DIR=efield-$efield
   mkdir -p $DIR

   cd $DIR

   #change pert.in
   cp ../../dynamics-run/efield-${efield}/pert.in  ./pert.in

   if [ "$OS" == "MACOS" ]; then
      sed -i '' "s|.*calc_mode.*|  calc_mode            = 'dynamics-pp'|g"   pert.in
   elif [ "$OS" == "LINUX" ]; then
      sed -i "s|.*calc_mode.*|  calc_mode            = 'dynamics-pp'|g"   pert.in
   else
      echo OS not supported
   fi

   # link prefix_epr.h5 and prefix_tet.h5
      ln -sf ../../../qe2pert/${PREFIX}_epr.h5
      ln -sf ../../setup/${PREFIX}_tet.h5
      ln -sf ../../dynamics-run/efield-0/${PREFIX}_cdyna.h5

   # copy prefix.temper
   cp ../../setup/${PREFIX}.temper .

   # run perturbo.x
   perturbo.x -i pert.in > pert.out 

   echo Done $efield

   # wait for a short period of time.  
   #done, return to upper directory.   
   cd ..
 
   sleep 1
done
```

### Output

The output of the *dynamics-pp* calculation is the *gaas\_popu.h5* file which contains the average distribution as a function of energy and time. It will also output *gaas\_dynamics-pp.yml* which contains the drift velocities for the different time steps and electric field strengths. 


## 5. Plot Velocity-Field Curves 

Now that we have obtained the drift velocities, we need to extract this using the following python script which plots the velocity-field curve

```
import yaml
import numpy as np
import matplotlib.pyplot as plt


prefix = 'gaas'
efields = np.arange(0, 3000, 200)
nsnaps_per_run = 20

drift_vels = []

# yml file
yml_file = f'efield-3000/{prefix}_dynamics-pp.yml'

# Opening yml file
with open(yml_file, 'r') as stream:
    try:
        # Converts yaml document to python object
        dct = yaml.safe_load(stream)

    except yaml.YAMLError as e:
        print(e)

vels_efield = dct['dynamics-pp']['velocity']

for i, efield in enumerate(efields):
    if i == 0:
        vel_i = 0.0
    else:
        idx = i * nsnaps_per_run + (nsnaps_per_run - 1)
        vel_i = (-1.0) * vels_efield[idx]

    drift_vels.append(vel_i)

drift_vels = np.asarray(drift_vels) / 1e6

# Plot velocity-field curve
fig, ax = plt.subplots()
ax.plot((efields / 1000), drift_vels, ls='', marker='o')
ax.set_xlabel('E (kV/cm)')
ax.set_ylabel('$v_d$ (cm/s)')
plt.savefig('velocity-field_curve.png')
plt.show()
```

Again we run this with the simple python command

```
python plot_velocity_field_curve.py
```

This should give the following curve

![drift_velocity_curve](https://github.com/perturbo-code/perturbo-workshop-2023/blob/main/Hands-on4/images/drift_velocity_eq.png)


