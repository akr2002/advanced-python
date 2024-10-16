# Python program to count the number of lines in a file


def count_lines_in_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, "r") as file:
            # Initialize a counter for the number of lines
            line_count = 0
            # Iterate through each line in the file and increment the counter
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
filename = "demo.txt"
number_of_lines = count_lines_in_file(filename)

if isinstance(number_of_lines, int):
    print(f"The file '{filename}' contains {number_of_lines} lines.")
else:
    print(number_of_lines)
