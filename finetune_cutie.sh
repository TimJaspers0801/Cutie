#!/bin/bash

#SBATCH --nodes=1                                   # Specify the amount of A100 Nodes with 4 A100 GPUs (single GPU 128 SBUs/hour, 512 SBUs/hour for an entire node)
#SBATCH --ntasks=1                                  # Specify the number of tasks
#SBATCH --cpus-per-task=64                          # Specify the number of CPUs/task (72)
#SBATCH --gpus-per-node=4
#SBATCH --partition=gpu_h100                             # Specify the node partition (see slides Cris)
#SBATCH --time=24:00:00                             # Specify the maximum time the job can run (120:00:00)

srun apptainer exec --nv /gpfs/home1/tjaspers2/Cutie/cutie.sif torchrun --master_port 25357 --nnodes 1 --nproc_per_node=4 cutie/train.py exp_id=0002 model=base data=SurgeSAM pre_training.enabled=False weights=/gpfs/home1/tjaspers2/Cutie/weights/cutie-base-mega.pth