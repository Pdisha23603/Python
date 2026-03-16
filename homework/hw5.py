# ask user about the start & end value & print accoundly to increment number

# a = int(input("enter the starting number: "))
# b = int(input("enter the ending number: "))
# c = int(input("enter the increment number by: "))
# for i in range(a,b,c):
#     print(i)

# 1.1 advance/increment version
# a = int(input("enter the starting number: "))
# b = int(input("enter the ending number: "))
# c = int(input("enter the increment number by: "))
# if c >= 0:
#     for i in range(a,b,c):
#         print(i)
# else:
#     print("enter valid number")

# 1.2 decrement version
# a = int(input("enter the value of starting point:"))
# b = int(input("enter the value of ending point:"))
# c = int(input("enter the decrement number b: "))
# if c <= 0:
#     for i in range(a,b,c):
#         print(i)
# else:
#     print("enter valid number!!")



# 1.2 combine both increment and decrement version
a = int(input("enter the starting point: "))
b = int(input("enter the ending point: "))
c = int(input("enter the value you want to incremeent or decrement: "))
if c <= 0:
    for i in range(a,b,c):
        print(i)
elif c >= 0:
    for i in range(a,b,c):
        print(i)
else:
    print("enter valid number!!")
