name = input("enter your name: ")
print(f"check ending words: {name.endswith("a")}") #check ending work but if there is space or dot(.) after character then it become false otherwise true
print(f"length: {len(name)}") #counting character
print(f"center the character: {name.center(20)}") 
print(f"left align: {name.ljust(20)}")
print(f"right align: {name.rjust(20)}")
print(f"count: {name.count("a")}")
