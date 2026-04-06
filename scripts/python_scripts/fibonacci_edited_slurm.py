#!/usr/bin/env python3

########### Change these variables to customize the job ###########
job_name   = "fibonacci.py"  # name of the job
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


print(f"import argparse")

####------------------ accept and parse command line arguments
# create an argument parser object
print(f"parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                in the Fibonacci sequence "))")

## add a positional argument, in this case, the position in the Fibonacci sequence
print(f"parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)")


## add optional argument for verbose output or not
# if 'store_true', this means assign 'True' if the optional argument is specified
# on the command line, so the default for 'store_true' is actuallt false
print(f"parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')")



## parse the argument
print(f"args = parser.parse_args()")
# initialize two integers
print(f"a,b = 0,1")

print(f"for i in range(int(args.position)):")
    print(f"a,b = b,a+b")
    
print(f"fibonacci_number = a")    

print(f"if args.verbose:")"
    print(f"print(f"The Fibonacci number for {args.position} is {fibonacci_number}.")")
print(f"else:")
    print(f"print(fibonacci_number)")  
