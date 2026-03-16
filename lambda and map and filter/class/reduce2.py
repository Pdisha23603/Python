# find sum of square of all even numbers from functools import reduce

# from functools import reduce
# def checkEven(num):
#     return num%2==0

# ans = reduce(checkEven,[1,2,3,4,5,6,7,8,10,11,12,15,16])
# print(ans)

# def sq(num):
#     return num*num
# sq_ans = reduce(sq,[ans])
# print(sq_ans)


from functools import reduce
numbers = [1,2,3,4,5,6,7,8,10,11,12,15,16]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers)) 
squared_evens = map(lambda x: x * x, even_numbers)
print(list(squared_evens)) 
result = reduce(lambda a, b: a + b, squared_evens)
print(result)
