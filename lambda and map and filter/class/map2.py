
# index loop
lst_number = [1,2,3,4]
pow_number = [2,2,2,3]
ans = []
for i in range(len(lst_number)):
    # ans.append(pow(lst_number[i],pow_number[i]))
    ans.append(lst_number[i]**pow_number[i])
print(ans)

lst_number = [1,2,3,4]
pow_number = [2,2,2,3]
for i in range(len(lst_number)):
    ans = list(map(pow,lst_number,pow_number))
print(ans)


# function fere to celcius lst_f = [2,4,5]
# ans_lst_c (use map)





# filter

def chackEven(num):
    if num%2==0:
        return num
    
lst = [2,3,4,5,6,7,8,9]
ans = list(filter(chackEven,lst))
print(ans)

# using map
def chackEven(num):
    if num%2==0:
        return num
    
lst = [2,3,4,5,6,7,8,9]
ans = list(map(chackEven,lst))
print(ans)