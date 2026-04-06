#!/usr/bin/env python3

import argparse

###------ function to parse the command-line arguments
def get_args():
    ####------------------ accept and parse command line arguments
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                    in the Fibonacci sequence ")

    ## add a positional argument, in this case, the position in the Fibonacci sequence
    parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)


    ## add optional argument for verbose output or not
    # if 'store_true', this means assign 'True' if the optional argument is specified
    # on the command line, so the default for 'store_true' is actuallt false
    parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')

    ## parse the arguments and retun in two steps
    args = parser.parse_args()
    return args

    ## OR, parse the arguments and retun in one step
    #return parser.parse_args()


###------ function to calculate the Fibonacci number
def fib():
    # initialize two integers
    a,b = 0,1

    for i in range(int(beyonce.position)):
        a,b = b,a+b
        
    fibonacci_number = a    
    return fibonacci_number

###------ function to print the output
def print_output(output):
    if beyonce.verbose:
        print(f"The Fibonacci number for {beyonce.position} is {output}.")
    else:
        print(output)    


###------ define the main function
def main():
    fibnum = fib()
    print_output(fibnum)
    ## this print statement fwill not print variables to show why local varibale cannot be accessed from main function
    #print(a, b, fibonacci_number)
#### calling get_args() happens out here on its own
beyonce = get_args()

# set the environment for this script
# is this main (i.e., a standalone python script), or
# is this a Python module being called by another script
if __name__ == '__main__':
    main()
