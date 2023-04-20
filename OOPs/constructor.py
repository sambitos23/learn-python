class Person:

    # Default Constructor
    # def __init__(self):
    #     print("Hey I am a person")

    # Parameterized constructor
    def __init__(self, n, o):  # constractor pass the arguments and stored as a positional argument in __init__
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Sambit", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
