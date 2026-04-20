#parse_GFF.py
import argparse
import gff_functions

def main():
    # Setup the command line interface
    parser = argparse.ArgumentParser(description="Extract genes from a genome using GFF coordinates.")
    
    # Tell argparse to expect two file paths when the script is run
    parser.add_argument("fasta", help="Path to the genome FASTA file")
    parser.add_argument("gff", help="Path to the GFF file")
    
    # Capture the paths the user typed in the terminal
    args = parser.parse_args()

    # RUN: to Get the DNA string
    genome = gff_functions.read_fasta(args.fasta)

    # RUN: Use the DNA string + GFF file to find specific genes
    gene_list = gff_functions.read_gff(args.gff, genome)

    #RUN: Write those specific genes into the output file
    gff_functions.write_output(gene_list)

# main
if __name__ == "__main__":
    main()
