# substring method
import re
str1 = " this is a new day!"

new_str=re.sub("new","beautiful",str1)
print(new_str) # regular expressiion work with patten  (patten - user\d)

new_str = str1.replace("new","beatuiful")
# print(new_str) work on string not in patten 