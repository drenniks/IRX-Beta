#!/bin/bash
#SBATCH --job-name="IRX"
#SBATCH --output="IRX.%j.%N.out"
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

python IRX_faceon.py
python IRX_sideon.py