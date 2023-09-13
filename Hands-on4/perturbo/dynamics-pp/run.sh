#!/bin/bash

PREFIX='gaas'

# EFIELDS=(0 100 200 300 500 1000 2000 3000 4000 6000 8000) 
EFIELDS=(0 100)
 
# MPI and OpenMP variables
NODES=1
NPOOLS=1
OMP_THREADS=4

OS='MACOS'
# OS='LINUX'

for efield in ${EFIELDS[@]}
do
   echo dynamics-pp for Efield= $efield

   DIR=efield-$efield
   mkdir -p $DIR

   cd $DIR

   #change pert.in
   cp ../pert-ref.in  ./pert.in
   if [ "$OS" == "MACOS" ]; then
      sed -i '' "s|.*boltz_efield(1).*| boltz_efield(1)      = $efield.0|g"   pert.in
   elif ["$OS" == "LINUX" ]; then
      sed -i "s|.*boltz_efield(1).*| boltz_efield(1)      = $efield.0|g"   pert.in
   else
      echo OS not supported
   fi

   # link prefix_epr.h5 and prefix_tet.h5
      ln -sf ../../../qe2pert/${PREFIX}_epr.h5
      ln -sf ../../setup/${PREFIX}_tet.h5
      ln -sf ../../dynamics-run/${PREFIX}_cdyna.h5

   # copy prefix.temper
   cp ../../setup/${PREFIX}.temper .

   # # mpirun
   # export OMP_NUM_THREADS=$OMP_THREADS 
   # mpirun -n $NODES perturbo.x -npools $NPOOLS -i pert.in > pert.out

   echo Done $efield

   # wait for a short period of time.  
   #done, return to upper directory.   
   cd ..
 
   sleep 1
done
