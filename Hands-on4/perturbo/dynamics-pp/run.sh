#!/bin/bash

PREFIX='gaas'

# Test with two values first, then run full selection
# EFIELDS=($(seq 200 200 400))
# EFIELDS=($(seq 200 200 3000))
# EFIELDS=(0)
EFIELDS=($(seq 0 200 3000))
 
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
