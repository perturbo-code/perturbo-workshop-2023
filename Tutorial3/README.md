# Tutorial 3: From prefix_epr.h5 to BTE transport (GaAs)

## 1 - Transport prerequisite
### 1.1 Setup
```
calc_mode = 'setup'
```
In a new working folder (`/perturbo/setup/`):
* Create and modify the input file `pert.in`.
* Create `'prefix'.temper` file to specify the configuration(s) to be compute.
* Copy or softlink the `'prefix'_epr.h5` file from `qe2pert` step into the running directory.
* Run Perturbo:

```
# Bc my cpu has quad-core
export OMP_NUM_THREAD=4 
perturbo.x < pert.in > pert.out
```

Output:
* `'prefix'.temper` - Modified from input
* `'prefix'_tet.kpt`: k-pts lie in the chosen energy window.
* `'prefix'_tet.h5`
* `'prefix'.doping`: chem potentials and carrier conc. for each temper of interest.
* `'prefix'.dos`: density of states (no. states/eV)


### 1.2 Imaginary part of the self-energy ($Im[\Sigma]$)
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
perturbo.x < pert.in > pert.out
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
perturbo.x < pert.in > pert.out
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
perturbo.x < pert.in > pert.out
```
The output files are similar to `RTA` calculations.





