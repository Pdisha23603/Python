# inheritance is a feature of object-oriented programming that allows a new class
# inherit student with person class 
# connect student with person class same as Employees class with person class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def display(self):
        print(self.name,self.age)

class Employees(Person):
    pass
class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name,marks)  # calling parent class constructor
        self.marks=marks
class Manager(Employees):
    pass
e1=Employees("disha",20,95)
e1.display()
