#!/bin/bash
#SBATCH --job-name="halo_prop"
#SBATCH --output="halo_prop.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 48:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=daniellerenniks@gmail.com

module load python
module load scipy
cd $SLURM_SUBMIT_DIR


srun python halo_prop.py