a = int(input("enter the starting range: "))
b = int(input("enter the ending range: "))
for num in range(a,b):
    temp = 1
    for i in range(2,num):
        if num%i == 0 :
            temp = 1
            print(f"{num} is not prime number")
            break
        else:
            temp == 0
    if temp == 0:
        print(f"{num} is prime number")
