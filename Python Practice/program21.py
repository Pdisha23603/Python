# for i in range(1, 5):
#     for j in range(i):
#         print(j % 2, end=" ")
#     print()



rows = 4
for i in range(1, rows + 1):
    for j in range(i):
        if j % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# output
# 1
# 1 0
# 1 0 1
# 1 0 1 0