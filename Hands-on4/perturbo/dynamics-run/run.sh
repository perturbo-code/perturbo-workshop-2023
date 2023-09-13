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
