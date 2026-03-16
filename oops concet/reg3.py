import re
str1 = "user test user1 user2 userdisha user3"
ans = re.findall("user\d",str1)  # ["user1", "user2","user3"]
ans = re.findall("\duser\d",str1) # no output
print(ans)

str2 = "this is Tops Technology"
ans = re.search(r"[a-j]",str2)  # search give first occur
print(ans)
# r reatun for row
ans = re.findall(r"[a-j]",str2)
print(ans)
ans = re.search(r"[a-j]",str2) #search in between also
print(ans)
ans = re.match(r"[a-j]",str2) # match only first occurance
print(ans)

# interview que search and match


