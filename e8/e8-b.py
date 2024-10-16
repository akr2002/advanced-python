# Demonstrating different inbuilt file handling functions in Python


def file_handling_demo():
    # Step 1: Open a file in write mode ('w') and write content to it
    file = open("demo.txt", "w")
    file.write("Hello, this is a demonstration of file handling in Python.\n")
    file.write("We are exploring various inbuilt functions.\n")
    # Flushes the written content to the file immediately
    file.flush()
    print("Data written to 'demo.txt' successfully.")

    # Step 2: Close the file after writing
    file.close()

    # Step 3: Open the file in append mode ('a') and add more content
    file = open("demo.txt", "a")
    file.write("Appending more data to the existing file.\n")
    file.close()
    print("Data appended to 'demo.txt' successfully.")

    # Step 4: Open the file in read mode ('r') to read the contents
    file = open("demo.txt", "r")
    content = file.read()
    print("\nReading content from 'demo.txt':")
    print(content)

    # Step 5: Use the 'tell()' function to get the current position in the file
    position = file.tell()
    print(f"\nCurrent position in the file after reading: {position}")

    # Step 6: Use the 'seek()' function to move the file pointer to the beginning
    file.seek(0)
    print(f"\nFile pointer repositioned using seek(). Current position: {file.tell()}")

    # Step 7: Read the first line using 'readline()'
    first_line = file.readline()
    print(f"\nFirst line of the file using readline(): {first_line}")

    # Step 8: Read all lines using 'readlines()' (this returns a list of lines)
    file.seek(0)  # Reset pointer to the beginning again
    all_lines = file.readlines()
    print(f"\nAll lines of the file using readlines(): {all_lines}")

    # Step 9: Close the file after reading
    file.close()
    print("\nFile closed successfully.")


# Call the demonstration function
file_handling_demo()
