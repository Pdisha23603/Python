# find length of each element from list and display vowels from given string


lst_city = ['ahmedabad', 'surat', 'baroda', 'rajkot']
for city in lst_city:
    if 'a' in city or 'e' in city or 'i' in city or 'o' in city or 'u' in city:
        print(f"vowels in {city} are: ", end="")
        for i in city:
            if i in 'aeiou':
                print(i, end=" ")
        print()
    print(f"the length of {city} is {len(city)}")


# output
# vowels in ahmedabad are: a e a a 
# the length of ahmedabad is 9
# vowels in surat are: u a 
# the length of surat is 5
# vowels in baroda are: a o a 
# the length of baroda is 6
# vowels in rajkot are: a o 
# the length of rajkot is 6