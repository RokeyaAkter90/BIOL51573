#!/usr/bin/env python3

import my_function

def main():
    #print('Hello, world')
    input_name = input("Enter a name: ")

    my_function.greeting(input_name)
# set the environment for this script
# is is main(), or is this a module being called by someone else
if __name__ == '__main__':
    main()