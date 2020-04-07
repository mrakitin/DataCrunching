#!/bin/bash
#SBATCH -A covid-19
#SBATCH -p long
#SBATCH -t 2-00:00:00
#SBATCH -N 5
#SBATCH -J last100000

module unload gcc python

smiles_id_list_fn="ena79000to100000.smi"
protein_list_fn="protein_pocket_grid_list.txt"
total_blocks=20
nblocks_per_node=-$((${total_blocks}/${SLURM_JOB_NUM_NODES}))
  
module load gcc/6.4.0 python/3.6.5 /sdcc/covid19/dhidas/modulefiles/covid19

mkdir tasks
parallel -a ${smiles_id_list_fn} -a ${protein_list_fn} -j 1 "echo" > tasks/all_task_list.txt

parallel -a tasks/all_task_list.txt --delay 0.2 --pipepart --block ${nblocks_per_node} -j ${SLURM_JOB_NUM_NODES} "
    cat >> tasks/sub_task_{#}.txt; 
    srun -N 1 -n 1  --exclusive --cpus-per-task $((${SLURM_CPUS_ON_NODE}-1)) ./scripts/run_sub_par.sh tasks/sub_task_{#}.txt"

echo "Done"


