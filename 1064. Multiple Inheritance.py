class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name


o = DancerEmployee("Kathak", "Shivani")

print(o.name)  # Shivani
print(o.dance)  # Kathak

o.show()  # The name is Shivani

print(DancerEmployee.mro()) # [<class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]
# Value Search Order