class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.sound()
    
def add(a, b):
    return a + b

print(add(5, 3))       # integer
print(add("Hello ", "World"))  # string