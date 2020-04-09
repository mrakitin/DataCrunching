#!/bin/bash

echo process $1 $2 on `hostname`

module unload gcc python
module load gcc/6.4.0 python/3.6.5 /sdcc/covid19/dhidas/modulefiles/covid19
njobs=$(($SLURM_JOB_NUM_NODES*$SLURM_CPUS_ON_NODE))

../scripts/prepare_target.sh $2 
../scripts/smiles_dock.sh $2 $1 $3 $4 
../scripts/summarize.sh $1

