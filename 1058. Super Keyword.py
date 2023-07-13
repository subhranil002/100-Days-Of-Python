class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


rohan = Employee("Rohan Das", "420")

print(rohan.name) # Rohan Das
print(rohan.id) # 420

harry = Programmer("Harry", "2345", "Python")

print(harry.name) # Harry
print(harry.id) # 2345
print(harry.lang) # Python
