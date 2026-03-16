# Print no of digits and letters in String.Accept String from user. E.g string="H1Visa" Digits = 1 and letters=5

string = input("enter the string: ")
count_digit = 0
count_letter = 0
for i in string:
    if i.isdigit():
        count_digit += 1
    elif i.isalpha():
        count_letter += 1
print(f"digits = {count_digit} and letter = {count_letter}")


# output:
# enter the string: hr87y847ty524urjkfv
# digits = 8 and letter = 11