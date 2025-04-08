#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=9
#SBATCH --gpus=1
#SBATCH --partition=gpu_a100
#SBATCH --time=3:00:00


# Setup scratch-based cache/temp dirs
export CACHE_ROOT=$HOME/temp
export APPTAINER_CACHEDIR=$CACHE_ROOT
export APPTAINER_TMPDIR=$CACHE_ROOT/tmp
export TMPDIR=$CACHE_ROOT/tmp

mkdir -p "$APPTAINER_TMPDIR"



# Pull container from dockerhub
apptainer pull container.sif docker://tjmjaspers/cutie:v1
