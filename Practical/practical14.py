# Write a Python program to find the highest 3 values in a dictionary.


marks = {
    "Math": 85,
    "English": 92,
    "Science": 78,
    "History": 88,
    "Computer": 95
}

values = marks.values()
sorted_values = sorted(values, reverse=True)
ans = sorted_values[:3]
print("Highest 3 values are:",ans)

# output
# Highest 3 values are: [95, 92, 88]

