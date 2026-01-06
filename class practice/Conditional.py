# write a program of voting eligibility using conditional

age = int(input("enter the age: "))
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
print("\n")
age = int(input("enter the age: "))
weight = int(input("enter the weight: "))
if age>=18:
    if weight>=45:
        print("eligible for donating blood")
    else:
        print("uneligible for donating blood")
else:
    print("you are minor")

