#!/usr/bin/env python3
# =============================================================================
# parse_GFF.py
# Main entry point for the GFF parsing pipeline.
#
# Run from the command line like this:
#   python parse_GFF.py covid.fasta covid_genes.gff3
#
# The script will:
#   1. Read the genome sequence from the FASTA file.
#   2. Parse the GFF3 annotation file and extract each gene's sequence.
#   3. Write all sequences to covid_genes.fasta in FASTA format.
# =============================================================================

# 'import' brings in code from another file/library so we can use it here.

# argparse is a standard Python library that makes it easy to accept and
# validate command-line arguments. Without it we'd have to parse sys.argv
# ourselves, which is error-prone.
import argparse

# This imports ALL THREE functions we wrote in our own module.
# Because gff_functions.py lives in the same folder, Python can find it
# automatically. The dot-prefix notation (from . import) is not needed here.
from gff_functions import read_fasta, read_gff, write_output


def main():
    """
    Orchestrates the full pipeline:
      parse arguments → read FASTA → read GFF → write output
    """

    # -----------------------------------------------------------------------
    # 1. SET UP THE ARGUMENT PARSER
    #    ArgumentParser creates a helper object that knows what arguments
    #    the script expects. It also auto-generates a --help message.
    # -----------------------------------------------------------------------
    parser = argparse.ArgumentParser(
        description=(
            "Parse a genome FASTA file and a GFF3 annotation file, "
            "then write each annotated gene sequence to covid_genes.fasta."
        )
    )

    # Add the first positional argument: the FASTA file.
    # 'positional' means the user does NOT type a flag like --fasta;
    # they just provide the value in order on the command line.
    parser.add_argument(
        "fasta_file",           # name we use to access the value later
        help="Path to the genome FASTA file (e.g. covid.fasta)"
    )

    # Add the second positional argument: the GFF3 file.
    parser.add_argument(
        "gff_file",
        help="Path to the GFF3 annotation file (e.g. covid_genes.gff3)"
    )

    # Actually parse what the user typed on the command line.
    # After this call, args.fasta_file and args.gff_file hold the strings
    # the user provided.
    args = parser.parse_args()

    # -----------------------------------------------------------------------
    # 2. STEP-BY-STEP PIPELINE
    # -----------------------------------------------------------------------

    # --- Step 1: Read the genome sequence from the FASTA file ---
    print(f"Reading genome from: {args.fasta_file}")
    genome_sequence = read_fasta(args.fasta_file)

    # Quick sanity check: print the length of the genome so we can confirm
    # the file was read correctly. The SARS-CoV-2 genome is ~29,903 bp.
    print(f"  Genome length: {len(genome_sequence):,} bp")

    # --- Step 2: Parse the GFF3 file and extract gene sequences ---
    print(f"Parsing GFF3 file: {args.gff_file}")
    features = read_gff(args.gff_file, genome_sequence)

    print(f"  Features (genes/CDS) found: {len(features)}")

    # --- Step 3: Write results to covid_genes.fasta ---
    print("Writing output ...")
    write_output(features)


# ---------------------------------------------------------------------------
# This block ensures main() is called ONLY when the script is run directly
# (e.g., `python parse_GFF.py ...`), NOT when it is imported as a module
# by another script. This is a Python best-practice idiom.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
