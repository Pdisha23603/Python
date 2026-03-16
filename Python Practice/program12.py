# Accept and print number until user enter 0 (use while)

# num = int(input("enter the number: "))
# while num != 0:
#     print(f"number is {num}")
#     num = int(input("enter the number: "))
    

while True:
    num = int(input("enter the number: "))
    if num == 0:
        break
    print(f"number is {num}")
    num = int(input("enter the number: "))