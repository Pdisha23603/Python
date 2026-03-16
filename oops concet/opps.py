# class : blueprint of object
# object
# inherantance : 
# encapsulation
# polymorphisum
# abstract



# directly not support overloading, indirectly support
# abstract object is not there

# class and object
# class: blueprint - structure - not actual entitie
# it is a collection of object
# it have a data member/state and member function/behaviour


# object: real entity
# it is type of class


# init: to initilize object , it call automatically, when create a object


class Person:
    def __init__(self,name,age,contact):
        print("welcome to OOPs")
        self.name=name
        self.age=age
        self.contact=contact
        
    def greet(self):
        print("Good Morning!",self.name,self.age,self.contact)
    def DisplayDetails(self):
        print(self.name,self.age,self.contact)
obj1 = Person("disha",21,23432343)
# obj1.greet("disha")
obj1.greet()
obj1.DisplayDetails()

obj2 = Person("abhay",20,23444432)
# obj2.greet("abhay")
obj2.greet()
obj2.DisplayDetails()

