# Tutorial 3: From `prefix_epr.h5` to Boltzmann Transport Equation (BTE)

## Galium Arsenide
GaAs is a polar semiconductor with a direct gap of ~1.42 eV at the $\Gamma$ valley. The challenge with this material is the long-range coupling between electron and the LO phonons, which makes it difficult for converging transport calculation. Additionally, in GaAs, electron-2-phonon scattering proccesses is also an important factor, as we shall see in this tutorial.

![image](https://github.com/perturbo-code/perturbo-workshop-2023/assets/85775106/a3e40d0c-e054-4d7f-85f9-5d0e08448106)

Below is the zoomed in energy window which will be taken into account for transport: a small region near the CBM @ ~6.025 eV.

![image](https://github.com/perturbo-code/perturbo-workshop-2023/assets/85775106/4366daf9-2de6-41ff-ace0-c642f536770a)

More details can be found at:

[1] J.-J. Zhou, M. Bernardi

Ab initio Electron Mobility and Polar Phonon Scattering in GaAs.
[Physical Review B (Rapid Communication) 2016 94, 201201](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.94.201201)

[2] N.-E. Lee, J.-J. Zhou, H.-Y. Chen, M. Bernardi 

Ab Initio Electron-Two-Phonon Scattering in GaAs from Next-to-Leading Order Perturbation Theory.
[Nature Communications 2020 11, 1607](https://www.nature.com/articles/s41467-020-15339-0)

---

## 1 - Transport prerequisite
Below is the general PERTURBO workflow. You can find the interactive version [here](https://perturbo-code.github.io/mydoc_interactive_workflow.html).

![Screenshot 2023-09-20 at 1 21 43 PM](https://github.com/perturbo-code/perturbo-workshop-2023/assets/85775106/4cab6e8b-444a-4eca-9e6b-933c66753ae5)

### 1.1 Setup
Before doing any transport calculation, we need to set up our energy window in a seperate calculation.
```
calc_mode = 'setup'
```
In a new working folder (`/perturbo/setup/`):
* Create and modify the input file `pert.in`.
* Create `'prefix'.temper` file to specify the configuration(s) to be compute.
* Copy or softlink the `'prefix'_epr.h5` file from `qe2pert` step into the running directory.
* Run Perturbo:

```
# Launch the job on 4 OMP threads
export OMP_NUM_THREAD=4 
perturbo.x -i pert.in > pert.out
```

Output:
* `'prefix'.temper` - Modified from input
* `'prefix'_tet.kpt`: k-pts lie in the chosen energy window.
* `'prefix'_tet.h5`
* `'prefix'.doping`: chem potentials and carrier conc. for each temper of interest.
* `'prefix'.dos`: density of states (no. states/eV)


### 1.2 Imaginary part of the self-energy ($Im[\Sigma]$)
One can learn some useful physical insights from the imaginary part of the self-energy. For our transport, this step is optional, but it will speed things up.
The result is used for computing the scattering rates / relaxation times in the subsequent steps.
```
calc_mode = 'imsigma'
```

In a new working directory (`/perturbo/imsigma/`):
* Copy or softlink the following file to this folder:
    * `'prefix'_epr.h5`
    * `'prefix'_tet.kpt`
    * `'prefix'.temper`
* Create and modify the input file `pert.in`.
* Run Perturbo:
```
export OMP_NUM_THREAD=4
perturbo.x -i pert.in > pert.out
```
Output:
* `'prefix'.imsigma`: computed $Im[\Sigma]$
* `'prefix'.imsigma_mode`: similar but with phonon mode indices

Now we are ready for transport.

---

## 2 - Transport

### 2.1 Relaxation time approximation (RTA)
```
calc_mode = 'trans-rta' or 'trans-mag-rta'
```

In a new working folder (`/perturbo/trans-rta-electron`):
* Create, or copy or soft-link the following:
    * `'prefix'_epr.h5`
    * `'prefix'_tet.h5`
    * `'prefix'.temper`
    * `'prefix'.imsigma` - Used previous $Im[\Sigma]$ result to obtain the relaxation times. (Optional)
* Create and modify the input file `pert.in`.
* Run Perturbo:
```
export OMP_NUM_THREAD=4
perturbo.x -i pert.in > pert.out
```
Output:
* `'prefix'.cond`: the conductivity and mobility tensors for each configuration
* `'prefix'.tdf`: transport distribution function (TDF) as a function of carrier energy and temperature
* `'prefix'_tdf.h5`: all the information of the TDF and occupation changes for each configuration in HDF5 format
* `'prefix'.trans_coef`: the conductivity, mobility, Seebeck coefficient and thermal conductivity tensors
### 2.1 Iterative time approximation (ITA)
```
calc_mode = 'trans-ita' or 'trans-mag-ita'
```

In a new working folder (`/perturbo/trans-rta-electron`):
* Create, or copy or soft-link the following:
    * `prefix_epr.h5`
    * `prefix_tet.h5`
    * `prefix.temper`
* Create and modify the input file `pert.in`.
* Run Perturbo:
```
export OMP_NUM_THREAD=4
perturbo.x -i pert.in > pert.out
```
The output files are similar to `RTA` calculations, as explained in previous section.





