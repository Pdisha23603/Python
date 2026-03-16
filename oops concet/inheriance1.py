class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal): #
    def bark(self):
        print("Dog bark")
d = Dog()
d.speak()
d.bark()