# key and value method
dict1 = {"india":"delhi","usa":"washington dc","uk":"london"}
print(dict1)
print(dict1.items())
print("iterating keys")
for i in dict1.keys():
    print(i)
print("iterating values")
for i in dict1.values():
    print(i)
print("iterating keys and values")
for i,j in dict1.items():
    print(i,j)

