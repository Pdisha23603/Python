# num = int(input("enter the number: "))
# n = 1
# for i in range(1, num + 1):
#     for j in range(i):
#         print(n, end = " ")
#     print()
#     n += 2


# output
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9 





num = int(input("enter the number: "))
n = 1
for i in range(1, num + 1):
    for j in range(i):
        print(n, end = " ")
        n += 2
    print()
    

# output
# 1 
# 3 5 
# 7 9 11 
# 13 15 17 19 
# 21 23 25 27 29 