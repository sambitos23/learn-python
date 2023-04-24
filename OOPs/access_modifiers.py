# Public Access Modifier
class Employee:
    def __init__(self):
        self.name = "Sambit"


a = Employee()
print(a.name)


# Private Access Modifier
class Employee:
    def __init__(self):
        self.__name = "Sambit Saha"  # using __ it can use as private (Weak internal use indicator)


a = Employee()
# print(a.__name)  -> We can not use this directly
print(a._Employee__name)  # We can access indirectly


# Name mangling
class MyClass:
    def __init__(self):
        self._private_attribute = "I am a private attribute"
        self.__mangled_attribute = "I am mangled attribute"

my_object = MyClass()

print(my_object._private_attribute)
# print(my_object.__mangled_attribute)  ->  Throws an Attribute error
print(my_object._MyClass__mangled_attribute)


# Protected Access Modifier
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):  # protected method
        return "CodeWithHarry"


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()


# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
