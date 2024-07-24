import argparse

def sort_lines(input_file):
    output_file = 'sorted_output.txt'

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Remove empty lines
    non_empty_lines = [line for line in lines if line.strip()]

    # Sort the lines alphabetically
    sorted_lines = sorted(non_empty_lines)

    # Write the sorted lines to a new file, ensuring each line ends with a newline character
    with open(output_file, 'w') as file:
        for line in sorted_lines:
            file.write(line if line.endswith('\n') else line + '\n')

    print(f"The lines have been sorted and written to {output_file}.")

def main():
    parser = argparse.ArgumentParser(description='Sort lines in a text file alphabetically and remove empty lines.')
    parser.add_argument('input_file', type=str, help='The input file to be sorted.')
    args = parser.parse_args()
    sort_lines(args.input_file)

if __name__ == "__main__":
    main()
