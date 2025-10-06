
#Task 2: Write and Append Data to a File
# Take user input and write it to output.txt
text_to_write = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(text_to_write + '\n')
print("Data successfully written to output.txt.\n")

# Take additional input and append to the same file
text_to_append = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(text_to_append + '\n')
print("Data successfully appended.\n")

# Read and print the final content of the file
print("Final content of output.txt:")
with open('output.txt', 'r') as file:
    print(file.read())
