class Animal:

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):

    def make_sound(self):
        print("Bark!")
        super().make_sound()


a = Animal() 
a.make_sound() # Sound made by the animal

d = Dog()
d.make_sound() 
# Bark!
# Sound made by the animal
