# Print list of items iteratively among with type of data e.g lst_collection = ['A',True,234,45.76] output = A - chr
#  True - bool
#  234 - int
# 45.76 - float

lst1= ['A', True, 234, 45.76]
for item in lst1:
    print(f"{item} = {type(item)}")