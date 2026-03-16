name = input("enter your name: ")
print(f"{name.find("a")}")  #find method
print(f"{name.replace("a","i")}") #replace method
print(f"{name.strip()}")  #trim -> strip() :. remove space from both side(right and left)
print(f"left side: {name.lstrip()}")  #ltrim -> lstrip() :. remove space from left side only 
print(f"right side: {name.rstrip()}")  #rtrim -> rstrip() :. remove space from right side only
print(f"startswith: {name.startswith("di")}")  # it count space also if you put space and start writing so it return false & without space you write then it become true