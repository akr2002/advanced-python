# Writing to a file
def write_to_file(filename, content):
    try:
        # Open the file in write mode ('w' will overwrite the file if it exists)
        with open(filename, "w") as file:
            file.write(content)
        print(f"Content written to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# Reading from a file
def read_from_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File {filename} not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"


# Example usage
filename = "example.txt"
content_to_write = "This is a sample text to be written to the file."

# Writing content to the file
write_to_file(filename, content_to_write)

# Reading content from the file
file_content = read_from_file(filename)
print("File content:")
print(file_content)
