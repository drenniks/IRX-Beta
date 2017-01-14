#!/bin/bash
#SBATCH --job-name="pynbody_images"
#SBATCH --output="pynbody_images.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 06:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=daniellerenniks@gmail.com

source ~/src/halo_database/environment.sh
source ~/src/halo_database/environment_local.csh

module load python
module load scipy
cd $SLURM_SUBMIT_DIR

python pynbody_try.py 


