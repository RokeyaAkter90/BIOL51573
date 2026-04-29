#! /scrfs/apps/python/anaconda3-2024.02-1/bin/python

########### Change these variables to customize the job ###########
job_name   = "watermelon.blast.rokeyaa"  # name of the job
partition  = "cloud72"  # name of the partition
nodes      = 1          # no of nodes /N
cpus       = 16         # requested cpus for the job
qos        = "cloud"    # name of the queue
time       = "01:00:00" # reqested wall time
email      = "rokeyaa@uark.edu"
##################################################################

# Python builds the slurm script by printing each line
print("#!/bin/bash")
print()
print(f"#SBATCH --job-name={job_name}")
print(f"#SBATCH --partition={partition}")
print(f"#SBATCH --nodes={nodes}")
print(f"#SBATCH --cpus-per-task={cpus}")
print(f"#SBATCH --qos={qos}")
print(f"#SBATCH --time={time}")
print("#SBATCH -o %x.%j.out")
print("#SBATCH -e %x.%j.err")
print("#SBATCH --mail-type=BEGIN,END,FAIL")
print(f"#SBATCH --mail-user={email}")
print()
print(f"export OMP_NUM_THREADS={cpus}   # for parallel cpus")
print()
print("module purge                                      # clean environment")
print("module load intel/18.0.1 impi/18.0.1 mkl/18.0.1   # required modules")
print("module load XXX                                   # required module")
print()
print("# cd to $SLURMM_SUBMIT_DIR")
print("cd $SLURM_SUBMIT_DIR")
print()
print("# copy files to to scratch")
print("cp XXXXX /scratch/$SLURM_JOB_ID  # files/folders to be copied")
print()
print("# cd onto the scratch disk to run the job")
print("cd /scratch/$SLURM_JOB_ID")
print()
print("# run the  command here")
print("COMMAND")
print()
print("# copy output back to $SLURM_SUBMIT_DIR")
print("rsync -arlv * $SLURM_SUBMIT_DIR/")
