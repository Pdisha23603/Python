# find length of each element from list

lst_city = ['ahmedabad', 'surat', 'baroda', 'rajkot']
for city in lst_city:
    print(f"the length of {city} is {len(city)}")


# find length of each element from list and display vowels in each element

lst_city = ['ahmedabad', 'surat', 'baroda', 'rajkot']
for city in lst_city:
    print(f"the length of {city} is {len(city)}")

for city in lst_city:
    for j in city:
        if j in "aeiouAEIOU":
            print(f"vowel in{city}")
            break
    