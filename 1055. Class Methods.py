class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(self, newCompany):
        self.company = newCompany


e1 = Employee()

e1.name = "Subhranil"
e1.changeCompany("Tesla")

e1.show() # The name is Subhranil and company is Tesla
