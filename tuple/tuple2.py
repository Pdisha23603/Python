#list of pair state and city

tuple_state_city = [("gujarat", "ahmedabad"), ("maharashtra", "mumbai"), ("rajasthan", "jaipur"), ("panjab", "amritsar")]
print(tuple_state_city[2])
print(tuple_state_city[2][1])

# fatch all capital of tuple of list
for state, city in tuple_state_city:
    print("capital of", state, "is", city)
