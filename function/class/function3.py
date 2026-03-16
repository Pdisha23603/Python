#fun with 2 parameter and return value
# pass 2 value and return sum
def greet():
    print("Have a nice day")

def greet1(name):
    print("Have a nice day",name)

def add(no1,no2):
    return no1+no2

greet()
greet1("ami")
greet1("abhay")
greet1("kinjal")

ans = add(23,11)
print(f"sum is: {ans}")