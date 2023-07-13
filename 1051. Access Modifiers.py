class Employee:
    def __init__(self):
        self.name1 = "Hey"
        self.__name2 = "Subhranil"  # Private


a = Employee()

print(a.name1) # Hey

# print(a.name) # AttributeError: 'Employee' object has no attribute 'name'

# print(a.__name2) # AttributeError: 'Employee' object has no attribute '__name2'

print(a._Employee__name2)  # Subhranil
