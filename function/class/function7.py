# keyword argunment
# it is giving dictionary
def employeeInfo(**kwargs):
    print(kwargs)
employeeInfo(name="disha",address="himmatnagar")
employeeInfo(name="disha",salary = 20000)
employeeInfo(dept="ds", master = "python")
# itrate
def employeeInfo(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
employeeInfo(name="disha",address="himmatnagar")
employeeInfo(name="disha",salary = 20000)
employeeInfo(dept="ds", master = "python")


