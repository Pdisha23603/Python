# accouding to exception the except block will executed
# try:
#     num = int(input("enter a number: "))
#     print(12/0)
# except ZeroDivisionError:
#     print("number can not divide by zero")
# except ValueError:
#     print("input mismatch")


try:
    num = int(input("enter a number: "))
    print(12/2)
    data =  {"name":"disha" }
    print(data("age"))
except ZeroDivisionError:
    print("number can not divide by zero")
except ValueError:
    print("input mismatch")
except: # except only execute when the is error inside program
    print("Error in try")
else:
    print("this is else block")
finally:
    print("have a nice day") # finally always execute if even ther is a problem in program



