#file open
#read : read(), readline() , readlines()
#write
#close

file = open("path locaytion") # we have to you \\(doble sless) for path
# c\\Users\\download\\notes.txt  <- simple location example
path = "location or path"
file = open(path)
print(file)
data = file.read() # read string
print(data)


