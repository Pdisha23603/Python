#slicing

name = input("enter name: ")
print(name[0:5]) #letter fron 0 to 5
print(name[:7])  #letter upto 7
print(name[7:]) # letter from 7 to end
print(name)

# use step
print(name[::2]) 
print(f" use negative indexing {name[-9: -2]}")  #negative index
print(f" use negative indexing {name[-9: -2: 3]}")  #negative index

# reverse string
print(name[::-1])