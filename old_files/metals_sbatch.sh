#!/bin/bash
#SBATCH --job-name="stars_metals"
#SBATCH --output="stars_metals.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 48:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=daniellerenniks@gmail.com

module load python
module load scipy

python stars_metals.py
