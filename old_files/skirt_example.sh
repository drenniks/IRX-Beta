#!/bin/bash
#SBATCH --job-name="skirt"
#SBATCH --output="skirt.%j.%N.out"
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


/home/u14266/src/SKIRT/release/SKIRTmain/skirt /oasis/scratch/comet/drenniks/temp_project/1945/Zubko/Zubko_0.ski

/home/u14266/src/SKIRT/release/SKIRTmain/skirt /oasis/scratch/comet/drenniks/temp_project/1945/nodust/nodust_0.ski


