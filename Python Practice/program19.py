# Write a program to display numbers which are divisible by 13 from given range.
start = int(input("enter the starting no: "))
end = int(input("enter the ending no:"))
for i in range(start, end + 1):
    if i % 13 == 0:
        print(f"{i} is divisible by 13")