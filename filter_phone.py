def filter_uniques(input_file, output_file):
    # Open the input file for reading and the output file for writing
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Use a set to keep track of unique lines
        unique_lines = set()
        # Loop through each line in the input file
        for line in f_in:
            # Strip any leading or trailing whitespace
            line = line.strip()
            # If the line is not already in the set of unique lines, add it to the set and write it to the output file
            if line not in unique_lines:
                unique_lines.add(line)
                f_out.write(line + '\n')

filter_uniques("phone_no.txt","filterd_phone_no.txt")