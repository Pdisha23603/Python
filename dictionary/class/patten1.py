# num = int(input("enter number: "))
# n=1
# for i in range(0,num):
#     #  if j%2==0:
#     #         print("1", end=" ")
#     #     else:
#     #         print("0", end=" ")
#     for j in range(i):
#        print(n, end = " ")
#        n+=2
#     print()

# star patten practical 25:

num = int(input("enter number: "))
for i in range(num*2):
    if i <= num:
        for j in range(i+1):
            if j==num:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            if i%2==0:
                print("*",end=" ")

        print()