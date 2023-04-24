class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"The name of Employee: {self.id} is {self.name}")


e1 = Employee("Rohan Das", 400)
e1.show_details()

e2 = Employee("Sambit Saha", 401)
e2.show_details()

print("============================")


class Programmer(Employee):
    def show_language(self):
        print("The default language is Python")


e2 = Programmer("Sambit Saha", 401)
e2.show_details()
e2.show_language()
