#assignment gff_functions.py
#read
def read_fasta(fasta_path):
    #Step Read the genome file.
    genome_sequence = ""
    
    # Open the file for reading ('r')
    with open(fasta_path, 'r') as file:
        
        # Skip the header (starts with '>'), so we skip it
        next(file)
        
        # Loop through each remaining line of DNA in the file
        for line in file:
            # .strip() removes the invisible '\n' (newline) at the end of each line
            # We add the cleaned line to our growing genome_sequence string
            genome_sequence += line.strip()
            
    # Return the full string of DNA
    return genome_sequence

###read_gff
def read_gff(gff_path, genome_sequence):
    #Parse the GFF and extract gene sequences.
    extracted_features = []

    with open(gff_path, 'r') as file:
        for line in file:
            # GFF files may have comment lines starting with '#'; we skip those
            if line.startswith("#") or not line.strip():
                continue

            # Split the line by Tabs ('\t') to get a list of columns
            cols = line.strip().split("\t")
            
            # Column 4 (index 3) is 'start', Column 5 (index 4) is 'end'
            start = int(cols[3]) - 1
            end = int(cols[4])
            
            # Use string slicing [start:end] to cut the specific gene out of the genome
            feature_seq = genome_sequence[start:end]
            
            # Column 9 (index 8) contains attributes
            attributes = cols[8]
            seq_id = ""
            
            # Split the attributes by semicolon to isolate the ID part
            for attr in attributes.split(";"):
                if attr.startswith("ID="):
                    # Remove 'ID=' to keep only the actual identifier
                    seq_id = attr.replace("ID=", "")
            
            # Save the ID and its corresponding DNA sequence as a pair (tuple)
            extracted_features.append((seq_id, feature_seq))
            
    return extracted_features

#write output
def write_output(features):
    #Save the results to a new file.

    output_filename = "covid_genes.fasta"
    
    # Open the output file for writing ('w')
    with open(output_filename, 'w') as out_file:
        # Loop through our list of ID/Sequence pairs
        for seq_id, sequence in features:
            # Write the header line with a '>'
            out_file.write(f">{seq_id}\n")
            # Write the DNA sequence on the next line
            out_file.write(f"{sequence}\n")
    
    print(f"Success! {len(features)} genes written to {output_filename}")
