#!/bin/bash
#SBATCH --job-name="skirt_halo"
#SBATCH --output="skirt_halo.%j.%N.out"
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


/home/u14266/src/SKIRT/release/SKIRTmain/skirt /oasis/scratch/comet/drenniks/temp_project/IRX/z_0/Zubko/Zubko_0.ski

/home/u14266/src/SKIRT/release/SKIRTmain/skirt /oasis/scratch/comet/drenniks/temp_project/IRX/z_0/no_dust/nodust_0.ski