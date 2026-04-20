#!/usr/bin/env python3

import argparse

def main():
    # create an argument parser object
    parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract whole exon sequences from the genome fasta file')

    # add positional arguments
    parser.add_argument("fasta", help='name of the FASTA file')
    parser.add_argument("gff", help='name of the GFF file')

    args = parser.parse_args()

    print(f'Genome fasta file:{args.fasta}')
    print(f'GFF file:{args.gff}')

 
# set the environment for this script
# is is main(), or is this a module being called by someone else
if __name__ == '__main__':
    main()