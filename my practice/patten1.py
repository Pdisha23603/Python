num = int(input("enter the number: "))
for i in range(num):
    for j in range(num, i ,-1):
        print(j, end = " ")
    print()



# output
# 5 4 3 2 1 
# 5 4 3 2
# 5 4 3
# 5 4
# 5