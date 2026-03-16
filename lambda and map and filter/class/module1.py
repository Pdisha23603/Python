# python has both standard modules and third-party modules
# standard modules are those which come with python installation
# third-party modules are those which we have to install using pip
# types
# standard modules
# user-defined modules
# third-party modules


def checkNumber(num):
    if num%2==0:
        return num
    
def checkPositive(num):
    if num>0:
        return "Positive"

def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact