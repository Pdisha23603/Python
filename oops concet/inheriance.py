# reusability
# parent child
# Person - Employees (single inheriance)
# Person - Employees - Manager (multi-level inheriance)
# Person - Employees 
#        -student (hierichical inheriance)
#  father - mother - child (multiple inheriance )

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def display(self):
        print(self.name,self.age)
class Employees(Person):
    pass
class Manager(Employees):
    pass

# e1.Employees("disha",20)
# e1.display()
