# same function name,different behaviour
# types : 1) compile time / method overloading & operator overloading

# method overloading means same method name but different argunment
# directly method overloading  is not supported in python through variable argunmnet it can achieved

# operator overloading 
# create point class
class Point:
    def __init(self,x,y):
        self.x = x
        self.y = y
    # def display(self):
    #     print(self.x,self.y)
    def __str__(self):
        return self.x,self.y
    def __add__(self, other):  # operator overloading
        # self.x=self.other.x
        # self.y=self.other.y
        # print(f"in add {self.x } and {self.y}")
        # return Point(self.x,self.y)
        p=Point(0,0)
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p
p1 = Point(12,23)
p2 = Point(2,3)
p3 = Point(0,0)
p3 = p1+ p2
p3.display()


# 2) runtime / method overriding
# method overridding : same method name, same parameter
class Student:
    def display(self):
        print(name,age)
class CollageStudent(Student):
    def display(self):
        print(name,age,semester)

