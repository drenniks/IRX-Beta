#!/bin/bash
#SBATCH --job-name="halo_characteristics"
#SBATCH --output="halo_characteristics.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 02:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=daniellerenniks@gmail.com


source ~/src/halo_database/environment_local.csh
source ~/src/halo_database/environment.sh

module load python
module load scipy
cd $SLURM_SUBMIT_DIR

python halo_characteristics.py > halo_characteristics.out


