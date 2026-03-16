# count no of strings which start with letter "M" from list

count = 0
lst_names = ["Mohit","Naresh","Harsh","meetali"]
for i in lst_names:
    if i.startswith("M"):
        print(i)
        count += 1
print(f"Total names starting with M: {count}")