lst1=["gujarat","rajasthan","punjab","odisha"]
lst2=["gandhinagar","jaipur","amritsar","bhubaneswar"]
ans = zip (lst1,lst2)
print(type(ans))    
print(list(ans))
print(tuple(ans)) #zip dont convert the iteration in tuple it only convert in list

lst1 = [1,2,3,4]
lst2 = [1,4,9,16]
lst3 = [1,8,27,64]
ans = list(zip(lst1,lst2,lst3))
print(ans)