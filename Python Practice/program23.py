# Print Pattern 
# 1
# 2  2
# 3  3  3
# 4  4  4 4

for i in range(1, 6):
    for j in range(i):
        print(i, end = "")
    print()

# output
# 1
# 22
# 333
# 4444
# 55555