#!/bin/bash

PREFIX='gaas'

# List of electric field strengths
EFIELDS=(0)
# EFIELDS=($(seq 200 200 1600))
# EFIELDS=($(seq 0 200 1600))

# OpenMP variable
OMP_THREADS=4

for efield in ${EFIELDS[@]}
do
   echo dynamics-run for Efield= $efield

   # Create directory efield-${field strength number}
   DIR=efield-$efield
   mkdir -p $DIR

   # Move into directory
   cd $DIR

   # Copy pert-ref.in into directory as pert.in
   cp ../pert-ref.in  ./pert.in

   # Change pert.in file
   # Change efield(1) parameter
   sed -i "s|.*boltz_efield(1).*| boltz_efield(1)      = $efield.0|g"   pert.in

   # If E != 0, set calculation to restart
   # and read e-ph matrix elements from file
   if [ $efield != 0 ]; then
      sed -i "s|.*boltz_init_dist.*| boltz_init_dist      = 'restart'|g"   pert.in
      sed -i "s|.*load_scatter_eph.*| load_scatter_eph      = .true.|g"   pert.in
   fi

   # link prefix_epr.h5 and prefix_tet.h5
   ln -sf ../../../qe2pert/${PREFIX}_epr.h5
   ln -sf ../../setup/${PREFIX}_tet.h5

   # copy prefix.temper
   cp ../../setup/${PREFIX}.temper .

   # If E != 0, link cdyna file for restart
   # and tmp file for e-ph matrix elements
   if [ $efield != 0 ]; then
      echo Linking cdyna and tmp
      ln -sf ../efield-0/${PREFIX}_cdyna.h5
      ln -sf ../efield-0/tmp
   fi

   # run pertubo.x
   export OMP_NUM_THREADS=${OMP_THREADS}
   perturbo.x -i pert.in > pert.out

   echo Done $efield

   # Return to upper directory
   cd ..
done
