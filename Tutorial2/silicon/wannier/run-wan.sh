#!/bin/bash 
#export OMP_NUM_THREADS=4
wannier90.x -pp si.win
pw2wannier90.x  < pw2wan.in > pw2wan.out
wannier90.x  si.win




