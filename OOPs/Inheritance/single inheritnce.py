class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"Sound made by the animal {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print(f"Bark! made by {self.breed}")


d = Dog("Dog", "Huskey")
d.make_sound()


a = Animal("Cat", "Pussy")
a.make_sound()
