class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails() # The name of Employee: 400 is Rohan Das

e2 = Employee("Harry", 4100)
e2.showDetails() # The name of Employee: 4100 is Harry

# e2.showLanguage() # AttributeError: 'Employee' object has no attribute 'showLanguage'

e3 = Programmer("Subhranil", 1111)
e3.showDetails() # The name of Employee: 1111 is Subhranil
e3.showLanguage() # The default langauge is Python