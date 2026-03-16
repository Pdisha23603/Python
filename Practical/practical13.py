# Write a Python program to sort a dictionary (ascending /descending) by value

marks = {
    "Math": 85,
    "English": 92,
    "Science": 78,
    "History": 88
}
# ascending order
asc = dict(sorted(marks.items(), key=lambda x: x[1]))
print("Ascending Order:", asc)
# descending order
desc = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print("Descending Order:", desc)

# output
# Ascending Order: {'Science': 78, 'Math': 85, 'History': 88, 'English': 92}
# Descending Order: {'English': 92, 'History': 88, 'Math': 85, 'Science': 78}