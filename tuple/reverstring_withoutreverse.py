# reverse a string without reverse function
string = "hello"
reverse = ""
for i in string:
    reverse = i + reverse
print(f"Reversed string: {reverse}")

# another method to reverse a string without reverse function
string = "world"
reverse = ""
for i in string:
    reverse = string[len(string)-1 - string.index(i)]
    print(reverse)

string = "world"
for i in range(len(string)-1, -1, -1):
    print(string[i], end="")    
print()
