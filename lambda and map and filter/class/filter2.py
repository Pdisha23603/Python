#  numbers are even then find a square
def checkEven(num):
    if num%2==0:
        return num
def sq(num):
    return num*num
lst_number = [1,2,3,4,5,6,7,8]
lst_even = list(filter(checkEven, lst_number))
lst_ans = list(map(sq,lst_even))
print(lst_ans)


# single line
lst_ans = list(map(sq,list(filter(checkEven, lst_number))))
print(lst_ans)