
lst_number = [1,2,3,4,5,6,7,8]
# lst_even = list(filter(checkEven, lst_number))
lst_ans = list(filter(lambda num:num%2==0 ,lst_number))
print(lst_ans)

lst = list(map(lambda num:num*num, lst_ans))
print(lst)