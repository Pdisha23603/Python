# compound interest
p = float(input("enter the principal amount: "))
r = float(input("enter the rate of interest: "))    
t = float(input("enter the time in year: "))
ci = p* (1+ r/100) **t -p   
print("compound interest is: ",ci)