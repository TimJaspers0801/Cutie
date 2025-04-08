#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=9
#SBATCH --gpus=1
#SBATCH --partition=gpu_a100
#SBATCH --time=3:00:00



APPTAINER_CACHEDIR=/gpfs/home1/tjaspers2/Cutie/temp/
# Pull container from dockerhub
apptainer pull container.sif docker://tjmjaspers/cutie:v1
