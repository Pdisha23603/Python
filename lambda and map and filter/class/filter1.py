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