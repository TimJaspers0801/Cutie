#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=9
#SBATCH --gpus=1
#SBATCH --partition=gpu_a100
#SBATCH --time=3:00:00


# Set a custom path where you have more disk space (e.g., on /scratch)
export MY_TMP_DIR=/gpfs/home1/tjaspers2/Cutie/temp/
mkdir -p "$MY_TMP_DIR"

# Set Apptainer/Singularity temp and cache directories
export APPTAINER_TMPDIR="$MY_TMP_DIR"
export APPTAINER_CACHEDIR="$MY_TMP_DIR"
export TMPDIR="$MY_TMP_DIR"  # Some tools still use this


# Pull container from dockerhub
apptainer pull container.sif docker://tjmjaspers/cutie:v1
