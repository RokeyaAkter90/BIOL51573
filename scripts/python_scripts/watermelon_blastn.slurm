#!/bin/bash

#SBATCH --job-name=watermelon.blast.rokeyaa
#SBATCH --partition=cloud72
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --qos=cloud
#SBATCH --time=01:00:00
#SBATCH -o %x.%j.out
#SBATCH -e %x.%j.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=rokeyaa@uark.edu

export OMP_NUM_THREADS=16   # for parallel cpus

module purge                                      # clean environment
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1   # required modules
module load blast                                 # required module

# cd to $SLURMM_SUBMIT_DIR
cd $SLURM_SUBMIT_DIR

# copy files to to scratch
cp watermelon.fsa /scratch/$SLURM_JOB_ID  # files/folders to be copied

# cd onto the scratch disk to run the job
cd /scratch/$SLURM_JOB_ID

# run the  command here
blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn

# copy output back to $SLURM_SUBMIT_DIR
rsync -arlv * $SLURM_SUBMIT_DIR/
