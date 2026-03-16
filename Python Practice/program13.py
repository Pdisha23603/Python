# Count number of digits in given number (e.g number=23456 o/p digits=5)

num = int(input("enter the number: "))
count = 0
if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count += 1
print(f"number of digits are {count}")