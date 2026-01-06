# different between is and ==

a = 5
b = 10
print(a == b)  # checks value equality, if both are same then returns True else False
print(a is b)  # checks object identity, if both are in same menory location then returns True else False
print(id(a))   # prints memory address of a
print(id(b))   # prints memory address of b
print("\n")
a = 10
b = 10
print(a==b)
print(a is b)