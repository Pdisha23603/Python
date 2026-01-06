a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = b
print(f"a is b: {a is b}")      #false because both are different object
print(f"a is not b: {a is not b}")  #true because both are different object
print(f"c is b: {c is b}")      #true because both are same object