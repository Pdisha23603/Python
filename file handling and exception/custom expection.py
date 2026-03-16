class PasswordLength(Exception):
    pass
try:
    password = input("enter a password: ")
    if len(password) < 8:
        raise PasswordLength
except PasswordLength:
    print("password must be greater than 8 letters")
# raise exception in both built-in or custom exception also!