age = int(input("enter the age: "))
weight = int(input("enter the weight: "))
if age>=18:
    if weight>=45:
        print("eligible for donating blood")
    else:
        print("uneligible for donating blood")
else:
    print("you are minor")
