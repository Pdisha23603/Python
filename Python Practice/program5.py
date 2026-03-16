# Find Compond Interest. Amount = P(1 + R/100) t  Compound Interest = A - P

P = int(input("enter the principal amount: "))
T = int(input("enter the time in years: "))
R = int(input("enter the rate of interest: "))
Amount = P*(1 + R/100)*T
# Compound Interest = A - P
print(f"componend Interest is: {Amount - P}")


# output:
# enter the principal amount: 23
# enter the time in years: 45
# enter the rate of interest: 12
# componend Interest is: 1136.2