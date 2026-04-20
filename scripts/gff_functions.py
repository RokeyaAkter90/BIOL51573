# =============================================================================
# gff_functions.py
# A module containing helper functions for parsing genome FASTA and GFF3 files.
# A "module" in Python is simply a .py file that holds reusable functions which
# can be imported into another script (like parse_GFF.py).
# =============================================================================


def read_fasta(fasta_file):
    """
    Opens a FASTA file and returns the full genome sequence as a single string.

    A FASTA file looks like this:
        >NC_045512.2 Severe acute respiratory syndrome ...   <- header line (skipped)
        ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACT...         <- sequence lines (kept)
        AGATCTTCAGAGAGTTCAAACTTTACTTGCTTTACATAGA...
        ...

    Parameters
    ----------
    fasta_file : str
        Path/name of the FASTA file to read (e.g. "covid.fasta")

    Returns
    -------
    genome_sequence : str
        The complete DNA sequence as one long string with no newlines.
    """

    # Start with an empty string; we will concatenate each line of DNA onto it.
    genome_sequence = ""

    # ------------------------------------------------------------------
    # 'open()' opens the file. Using 'with' ensures the file is
    # automatically closed when we are done, even if an error occurs.
    # 'r' means we are opening it for reading (not writing).
    # ------------------------------------------------------------------
    with open(fasta_file, "r") as f:

        # 'next(f)' advances the file object by one line, effectively
        # SKIPPING the first line (the ">" header line we don't need).
        next(f)

        # Now iterate over every remaining line in the file.
        for line in f:

            # '.strip()' removes any whitespace or newline characters
            # (\n) from both ends of the string.
            # Without this, our sequence would have embedded newlines
            # and string slicing later would give wrong results.
            genome_sequence += line.strip()

    # After the loop, genome_sequence is one continuous DNA string.
    return genome_sequence


# -----------------------------------------------------------------------------

def read_gff(gff_file, genome_sequence):
    """
    Reads a GFF3 annotation file and, for each annotated feature (gene/CDS),
    slices the corresponding subsequence out of genome_sequence.

    A GFF3 file has 9 tab-separated columns:
        Col 0  seqid      – chromosome / contig name
        Col 1  source     – program that produced the annotation
        Col 2  type       – feature type (e.g. "gene", "CDS")
        Col 3  start      – 1-based start coordinate  ← we need this
        Col 4  end        – 1-based end coordinate    ← and this
        Col 5  score      – numeric score or '.'
        Col 6  strand     – '+' or '-'
        Col 7  phase      – reading frame (0, 1, 2, or '.')
        Col 8  attributes – key=value pairs separated by ';'
                            e.g. "ID=cds-YP_009724389.1;Parent=gene-ORF1ab;..."

    Parameters
    ----------
    gff_file      : str  – path/name of the GFF3 file
    genome_sequence : str – the full genome string returned by read_fasta()

    Returns
    -------
    features : list of tuples
        Each tuple is (sequence_id, subsequence) for one annotated feature.
        Example: ("cds-YP_009724389.1", "ATGAGTGAT...")
    """

    # We will collect results here as a list of (id, sequence) tuples.
    features = []

    with open(gff_file, "r") as f:
        for line in f:

            # GFF3 files often start with comment/metadata lines that
            # begin with '#'. We skip those because they are not data rows.
            if line.startswith("#"):
                continue

            # Remove the trailing newline, then split on TAB characters.
            # After splitting, 'cols' is a list of 9 strings, one per column.
            cols = line.strip().split("\t")

            # Guard: skip any malformed lines that don't have 9 columns.
            if len(cols) < 9:
                continue

            # ----------------------------------------------------------
            # Extract start and end coordinates (columns 3 and 4).
            # GFF3 uses 1-based, fully-closed coordinates:
            #   start=1, end=10  means the first 10 nucleotides.
            # Python strings use 0-based, half-open slicing:
            #   sequence[0:10]   also gives the first 10 nucleotides.
            # So we convert: python_start = gff_start - 1
            #                python_end   = gff_end      (no change needed)
            # ----------------------------------------------------------
            start = int(cols[3])   # cast string "21563" → integer 21563
            end   = int(cols[4])   # cast string "25384" → integer 25384

            # Slice the genome string to get just this feature's sequence.
            # Python slicing: sequence[start_inclusive : end_exclusive]
            subsequence = genome_sequence[start - 1 : end]

            # ----------------------------------------------------------
            # Parse the sequence ID from the attributes column (col 8).
            # The column looks like:
            #   "ID=cds-YP_009724389.1;Parent=gene-ORF1ab;..."
            #
            # Step 1: split on ';' to get individual key=value pairs.
            # Step 2: loop through them to find the one starting with "ID=".
            # Step 3: strip off the "ID=" prefix to keep only the value.
            # ----------------------------------------------------------
            attributes = cols[8]           # e.g. "ID=cds-YP_009724389.1;..."
            sequence_id = None             # will be filled in below

            for attribute in attributes.split(";"):
                if attribute.startswith("ID="):
                    # Remove the "ID=" prefix (first 3 characters).
                    sequence_id = attribute[3:]
                    break  # we found what we need; no reason to keep looping

            # Only add the feature if we successfully parsed an ID.
            if sequence_id:
                features.append((sequence_id, subsequence))

    return features


# -----------------------------------------------------------------------------

def write_output(features, output_file="covid_genes.fasta"):
    """
    Writes all extracted gene sequences to a FASTA-formatted output file.

    FASTA format rules:
        Line 1 – header starting with '>'  followed by the sequence identifier
        Line 2+ – the DNA sequence (can be wrapped at 60 or 70 chars, but here
                   we write it as a single line for simplicity)

    Example output:
        >cds-YP_009724389.1
        ATGAGTGATGGTTTTAAAATGGTTTTTAATAAATTT...
        >cds-YP_009725295.1
        ATGGCTACATTTGTTCAGGGTTTTATTGTGAAGAAG...

    Parameters
    ----------
    features    : list of tuples – output from read_gff()
    output_file : str            – name of the file to create/overwrite
                                   (defaults to "covid_genes.fasta")
    """

    # 'w' opens the file for WRITING.
    # If the file already exists it will be overwritten.
    # If it does not exist it will be created.
    with open(output_file, "w") as out:

        # Unpack each tuple into its two components.
        for sequence_id, subsequence in features:

            # Write the FASTA header line.
            # f-strings (f"...") let us embed variables directly in a string.
            # '\n' is the newline character – moves to the next line.
            out.write(f">{sequence_id}\n")

            # Write the DNA sequence, followed by a blank line for readability.
            out.write(f"{subsequence}\n\n")

    # Let the caller know where the results ended up.
    print(f"Output written to: {output_file}")
