# add integer value from a list

lst_number = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in lst_number:
    if type(i) == int or type(i) == float:
        sum = sum + i  # sum += i 
print(f"The sum of the list is: {sum}")