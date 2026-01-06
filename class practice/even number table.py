
# multiplication table of even numbers using for loop
num = int(input("enter the number: "))
if num%2 == 0:
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
else:
    print("enter the even number only!!")


num = int(input("enter the number: "))
if num%2 ==0:
    while i<=10:
        print(f"{num} * {i} = {num*i}")
        i += 1
else:
    print("enter the even number only!!")