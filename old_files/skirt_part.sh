#!/bin/bash
#SBATCH --job-name="skirt_part"
#SBATCH --output="skirt_part.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 48:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=daniellerenniks@gmail.com

module load python
module load scipy

python skirt_stars.py
python skirt_gas.py