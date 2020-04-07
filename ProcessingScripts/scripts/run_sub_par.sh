#!/bin/bash


echo read task list from $1 with ${SLURM_CPUS_ON_NODE} processes
parallel -a $1 --timeout=3600000 --colsep '\s+' -j ${SLURM_CPUS_ON_NODE} "
    mkdir {2}_{#}; cd {2}_{#};
    cp ../data/{3}.pdb .;
    echo {1} {2} > {2}_smi.can; 
    ../scripts/run_all_crunch.sh {2}_smi.can {3} {4} {5} &> {2}_stdout.txt; 
    "


