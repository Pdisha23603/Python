# it return single value by appling a binary function  (takes two argumnents) (combine elements into one)
# from functools import reduce

from functools import reduce
def add(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

ans = reduce(mul,[1,3,5,7,9,11,13,15])
print(ans)

ans = reduce(add,[1,2,3,4,40,50])
print(ans)