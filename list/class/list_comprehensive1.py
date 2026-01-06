# lst1=["gujarat","rajastan","maharashtra"]
# ans = [i for i in lst1]
# print(ans)
# # print element whose len is moew then 5
# ans = [i for i in lst1 if len(i) > 7 ]
# print(ans)


# append
# lst1=["gujarat","rajastan","maharashtra"]
# ans = []
# for i in lst1:
#     ans.append(i)
# print(ans)

# write a program to find a square of a number and store it into another list
# lst2 = [1,22,6]
# ans = []
# for i in lst2:
#     ans.append(i**2)
# print(ans)

# lst2 = [1,22,6]
# ans = [i**2 for i in lst2 if i%2==0]
# print(ans)

# convert liust elemnets into uppercase
# lst3 =["gujarat","rajastan","panjab","maharashtra"]
# ans = [i.upper() for i in lst3]
# print(ans)

# tuple comprehensive
lst3 =(["gujarat","rajastan","panjab","maharashtra"])
ans = [i.upper() for i in lst3]
print(ans)
# tuple will give you generator