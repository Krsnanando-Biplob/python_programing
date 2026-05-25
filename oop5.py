# Parent Class
class Animal:
    
    def sound(self):
        print("Animal makes sound")


# Child Class
class Dog(Animal):
    
    def bark(self):
        print("Dog barks")


# Object create
d = Dog()

d.sound()
d.bark()  