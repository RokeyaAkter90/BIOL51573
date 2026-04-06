#!/usr/bin/env python3

def greeting(name):
    print(f'hello from the my_function() module, {name}')


def main():
    print('Hello, world')
# set the environment for this script
# is is main(), or is this a module being called by someone else
if __name__ == '__main__':
    main()