# seek and tell : used for telling position
# using readline method read whole file using while loop
file = open("C:\\Users\\disha\\python program\\lambda and map and filter\\class\\module1.py")
line = file.readline()
file.seek(15)
print(f"starting position {file.tell()}")

while line != "":
    print(line)
    line = file.readline()


# 2 method
while True:
    line = file.readline()
    print(line)
    if not line:
        break

# readlines
line = file.readlines()
print(line)
for i in line:
    print(i)

print(f"ending position {file.tell()}")