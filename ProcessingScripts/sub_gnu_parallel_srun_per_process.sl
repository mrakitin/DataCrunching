#!/bin/bash
#SBATCH -A covid-19
#SBATCH -p long
#SBATCH -t 2:00:00
#SBATCH -N 2

module unload gcc python

smiles_id_list_fn="ena+db-test.can"
protein_list_fn="protein_pocket_grid_list.txt"
  
module load gcc/6.4.0 python/3.6.5 /sdcc/covid19/dhidas/modulefiles/covid19
njobs=$(($SLURM_JOB_NUM_NODES*$SLURM_CPUS_ON_NODE))

parallel --delay 0.2  --colsep '\s+' -j $njobs -a ${smiles_id_list_fn} -a ${protein_list_fn} "
    mkdir {2}_{#}; cd {2}_{#};
    cp ../data/{3}.pdb .;
    echo {1} {2} > {2}_smi.can; 
    srun -N 1 -n 1 --exclusive ../scripts/run_all_crunch.sh {2}_smi.can {3} {4} {5} &> {2}_stdout.txt; 
"

echo "Done"
