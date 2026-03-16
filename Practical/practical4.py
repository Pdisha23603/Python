#  Write a Python program to get a single string from two given strings, separatedbya space and swap the first two characters of each string.

str1 = input("enter first string: ")
str2 = input("enter second string: ")
string1 = str2[:2] + str1[2:]
string2 = str1[:2] + str2[2:]
ans = string1 + " " + string2
print(ans)

# output
# enter first string: disha
# enter second string: patel
# pasha ditel