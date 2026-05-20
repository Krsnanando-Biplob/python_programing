class Student:
    
    # Constructor
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    
    # Method
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


s1 = Student("Rahim", 20, "CSE")

# Method call
s1.show_info()