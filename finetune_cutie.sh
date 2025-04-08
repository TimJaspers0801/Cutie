en dan had ik dit batch script gemaakt:

#!/bin/bash

#SBATCH --nodes=1                                   # Specify the amount of A100 Nodes with 4 A100 GPUs (single GPU 128 SBUs/hour, 512 SBUs/hour for an entire node)

#SBATCH --ntasks=1                                  # Specify the number of tasks

#SBATCH --cpus-per-task=72                          # Specify the number of CPUs/task (72)

#SBATCH --gpus-per-node=4

#SBATCH --partition=gpu                             # Specify the node partition (see slides Cris)

#SBATCH --time=02:30:00                             # Specify the maximum time the job can run (120:00:00)

source /gpfs/home1/rdejong/miniconda3/etc/profile.d/conda.sh

conda activate cutie

OMP_NUM_THREADS=4 torchrun --master_port 25357 --nproc_per_node=4 cutie/train.py exp_id=0002 model=base data=RAMIE pre_training.enabled=False weights=/gpfs/home1/rdejong/Cutie/weights/cutie-base-mega.pth
