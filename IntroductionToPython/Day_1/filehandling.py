# Open a file: Use the open() function to open a file.

file = open("filename.txt", "r")  # Opens in read mode


# Close a file: After performing file operations, use the close() method to close the file.

# file.close()


# Read from a file: To read the contents of a file, you can use methods like read(), readline(), or readlines().

# content = file.read()  # Reads the entire file content
# print(content)


# Write to a file: To write content to a file, you can use write() or writelines().

# file.write("This is a new line of text.")


# Append to a file: To add content to the end of an existing file, open it in append mode (a).

# file = open("filename.txt", "a")
# file.write("This line is appended.")