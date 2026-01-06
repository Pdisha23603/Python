# swap number
a = int(input("enter the first number: "))
b = int(input("enter the second number: " ))
c = a
a = b
b = c 
print("display the number after swaping the number: a =",a ,", b =",b)

# swap number without using third variable
a = int(input("enter the number a:"))
b = int(input("enter the number b: "))
a , b = b , a
print("display the number after swaping the number: a =",a ,", b =",b)


# swap number using arithmetic operation
a = int(input("enter the number a:"))
b = int(input("enter the number b: "))
a = a + b
b = a - b
a = a- b
print("display the number after swaping the number: a =",a ,", b =",b)









