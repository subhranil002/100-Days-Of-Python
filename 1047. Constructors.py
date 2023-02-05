# Old Method -->
# class Person:
#     name = "Subhranil"
#     occupation = "Software Developer"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
    
# a = Person()
# a.info() # Subhranil is a Software Developer
# a.name = "Harry"
# a.occupation = "Data Scientist"
# a.info() # Harry is a Data Scientist 


# Introducing Constructor -->
class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
Subhranil = Person("Subhranil", "Software Developer")
Harry = Person("Harry", "Data Scientist")
Subhranil.info() # Subhranil is a Software Developer
Harry.info() # Harry is a Data Scientist