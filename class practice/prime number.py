# num = int(input("enter the number: "))
# for i in range(2, num):
#     if num%i == 0:
#         print(f"{num} is not a prime number")
#         break
#     else:
#         print("{num} is a prime number")

num = int(input("enter the number: "))
temp=1
for i in range(2, num):
    if num%i == 0:
        temp=1  # temp is used for avoiding the multiple print statements
        print(f"{num} is not a prime number")
        break
    else:
        temp=0 #flag
if temp==0:
    print("is a prime number")