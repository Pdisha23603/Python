# num = int(input("enter number: "))
# for i in range(num): # i means row and j means colums
#     for j in range(i + 1):
#         print("*", end=" " ) # or print("*", end="\t")
#     print()


# num = int(input("enter number: "))
# for i in range(1,num+1): # i means row and j means colums
#     for j in range(1,i + 1):
#         print(i, end=" " ) # or print("*", end="\t")
#     print()


# reverse patten
num = int(input("enter the number: "))
for i in range(num): # i means row and j means colums
    for j in range(num,i,-1):
        print(i, end=" " ) # or print("*", end="\t")
    print()