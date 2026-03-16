import module1
ans = module1.fact(12)
print(ans)

# second way
from module1 import fact
ans = fact(5)
print(ans)


# call another function
from module1 import fact, checkNumber
ans = fact(5)
print(ans)

# 3 way 
import module1 as m1
print(m1.checkNumber(20))


# file in another folder
#  math,random,sys, datetime