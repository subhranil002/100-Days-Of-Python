class Person:
    name = "Subhranil"
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
print(a.name) # Subhranil

a.info() # Subhranil is a Software Developer

a.name = "Harry"
a.occupation = "Data Scientist"
a.info() # Harry is a Data Scientist 