# map
# find square of all number and return list of it
# return list of square of given list


# def sq(num):
#     return num*num
# sq_ans=[]
# lst = [1,2,3,4]
# for i in lst:
#     sq_ans.append(sq(i))
# print(sq_ans)


# make list of names
# name = [ "disha","riya","maitri","mansi"]
# name1 =[]
# for i in name:
#     name1.append(i.upper())
# print(name1)

# make list of names
name = [ "disha","riya","maitri","mansi"]
name1 =[]
# for i in name:
#     name1.append(i.upper())
name1 = list(map(str.upper,name1))
print(name1)



# def sq(num):
#     return num*num
# sq_ans=[]
# lst = [1,2,3,4]
# # for i in lst:
# #     sq_ans.append(sq(i))
# sq_ans = list(map(sq,lst))
# print(sq_ans)



#  base3_num = [1,2,3]
# power_num = [2,2,3]
# ans = [1,4,27,] try this using map and use inbuilt function