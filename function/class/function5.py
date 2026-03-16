# parameters
# 1. fefault argunment
# 2. variable argunment
# 3. keyword argunment

# 1. default argunment
def greet(msg="have a nice day"):
    print(msg)
def studentInfo(name,address,age = 20):
    print(name,address,age)
# rules of default
# default agunment should be at last.
def empInfo(name,c_no,salary,address="paldi"):
    print(name,address,c_no,salary)


greet("good morning")
greet("good afternoon")
greet()

studentInfo("disha","himmatnagar")
studentInfo("abahy","australia",19)
studentInfo()
