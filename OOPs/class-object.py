class Person:
    name = "Harry"
    occupation = "Software Developer"
    netWorth = 10

    def info(self):  # Wo object jiske liye method call kiya ja raha hai
        print(f"{self.name} is a {self.occupation}")


a = Person()
print(a.name, a.occupation)
a.info()

a.name = "Shubham"
a.occupation = "Accountant"
print(a.name, a.occupation)
a.info()
