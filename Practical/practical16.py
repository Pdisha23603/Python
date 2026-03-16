# Counting the frequencies in a list using a dictionary in Python. Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

numbers = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
freq = {}   # empty dictionary
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
# sorted order
for key in sorted(freq):
    print(key, ":", freq[key])


# output
# 1 : 5
# 2 : 4
# 3 : 3
# 4 : 3
# 5 : 2
