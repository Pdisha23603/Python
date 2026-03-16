# read from one file and write to another file(copy file)

# read : WITH keyword

# without using with keyword
file = open("C:\\Users\\disha\\python program\\file handling\\first.txt", "r")
dest = open("copy.txt", "w")
for line in file:
    dest.write(line)
file.close()
dest.close()
print("File copied successfully!")







#  using with keyword to read and write file
with open("C:\\Users\\disha\\python program\\file handling\\first.txt", "r") as src:
    with open("copy.txt", "w") as dest:
        for line in src:
            dest.write(line)
print("File copied successfully!")

# src.close() # no need to close file when we use with keyword
# 1) with open("source.txt", "r") as src:
# Opens source.txt in read mode (r)
# src is the variable used to read the file
# with automatically closes the file when work is done
# (you don’t need close())

#  2) with open("destination.txt", "w") as dest:
# Opens destination.txt in write mode (w)
# dest is the variable used to write to the file

# 3) for line in src:
# Iterates through each line in the source file (src)

# 4) dest.write(line)
# Writes the current line from the source file to the destination file (dest)

#  5) Files close automatically
# When with block ends:
# src file closes
# dest file closes

#  5) print("File copied successfully!")
# Prints a message indicating that the file has been copied successfully
