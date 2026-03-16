# JSON- in python json known as dictionary only 
# conbert python data structure(dictionary,tuple,set) in JSON format

# create an empty dictionary to store user input
import json
# user_data = {}
user_data = []

# Accept user input
# user_data["name"] = input("Enter your name: ")
# user_data["age"] = int(input("Enter your age: "))
# user_data["city"] = input("Enter your city: ")
# user_data1[
#     {"name"}
# ]
# open a JSON file in write mode
# with open("user_data.json","w") as file:
#     # write the dictionary to the file in JSON file
#     json.dump(user_data,file,indent = 4)   # indent = 4 it is optional
# print("data added successfully")

# diff bet dump and dumps
# dump is inbulit method user for writing into file.  method can be used for writting to JSON file
# dumps method can convert a python object into a JSON string

# open JSON in read mode
with open("user_data.json","r") as file:
    # write the dictionary to the file in JSON file
    user_data = json.load(file)   # load method is use for reading file
print(type(user_data))

# fetch data
for i in user_data:
    print(i)





# lab task: to add multiple data use loop and append method 