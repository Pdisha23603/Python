# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def unique_elements(lst):
    unique_lst = list(set(lst))
    return unique_lst
input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print("Unique elements in the list are:", result)

# output
# Unique elements in the list are: [1, 2, 3, 4, 5]
