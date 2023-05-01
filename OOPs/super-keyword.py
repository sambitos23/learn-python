# super() keyword in python used to refer to the parent class.

class ParentClass:
    def parent_method(self):
        print("This is the parent method")


class ChildClass(ParentClass):
    def parent_method(self):
        print("Sambit")
        super().parent_method()  # if we wanted to use parent method in child class, we have to use super keyword

    def child_method(self):
        print("This is a child method")
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
""" 
Output:
This is a child method
This is the parent method
"""

child_object.parent_method()
"""
Output:
Sambit
This is the parent method
"""


# =============================

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")

print(rohan.name)
print(harry.id)
