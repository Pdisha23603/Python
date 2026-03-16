# Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by theuser. 
# To generate a password, randomly take some words from the user input andtheninclude numbers, special characters
#  and capital letters to generate the password. Also, keep a check that password length is more than 8 characters.
#  Note: Include Exception handling wherever required. Also, make a ‘User’ classand store the details like user id,
#  name and password of each user as a tuple



import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.data = (user_id, name, password)  

    def display(self):
        print("User Details:", self.data)

def generate_password(text):
    try:
        words = text.split()

        if len(words) == 0:
            raise ValueError("Please enter some words")

        word = random.choice(words)

        number = str(random.randint(10,99))
        special = random.choice("!@#$%&*")
        password = word.capitalize() + number + special

        if len(password) < 8:
            password = password + "123@"

        return password

    except Exception as e:
        print("Error:", e)


try:
    user_id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    text = input("Enter some words to generate password: ")

    password = generate_password(text)

    user = User(user_id, name, password)
    user.display()

except ValueError:
    print("Invalid input. User ID must be a number.")

