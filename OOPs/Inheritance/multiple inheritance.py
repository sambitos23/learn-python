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


class DancerEmployee(Employee, Dancer):  # whatever method was written first (Employee) it will show
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name


o = DancerEmployee("Kathak", "Shivani")
print(o.name, o.dance)
o.show()
