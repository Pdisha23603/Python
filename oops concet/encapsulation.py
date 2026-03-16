# wrappingm up of data and function together
# data hiding
# use _ or __ to make variable private
# hide data is called encapsulation

class A:
    def __init__(self,contact):
        self.__contact=contact
        # self.name=name
    def display(self):
        print(self.contact,self.name)
a = A("disha",1234567)
a.display()
print(a.contact)


# _   :
# __  : private
#     : public

# labtask: put single underscore 

# when we have to display hidden data at that time we use getter and setter in encapsulation
