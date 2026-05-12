class Student:
    
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("------------------")


# object create
s1 = Student("Rahim", 20, "CSE")
s2 = Student("Karim", 22, "EEE")

# method call
s1.show_info()
s2.show_info()