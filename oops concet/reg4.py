# ^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-z]{2,3}$
# ^[a-zA-Z][0-9]+@[a-zA-Z]+\.[a-zA-z]{2,3}$


import re
str1 = "test@gmail.com disha2341@gmail.com"
ans = re.findall(r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-z]{2,3}$",str1)
print(ans)


# lab task: work on multiple email