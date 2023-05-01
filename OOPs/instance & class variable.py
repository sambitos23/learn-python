#  If we define a variable in class label -> Class Variable
#  If we define a variable in specific instance -> Instance Variable

class Employee:
    company_name = "Apple"  # class variable
    no_of_employee = 0  # class variable

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02  # instance variable
        Employee.no_of_employee += 1  # class variable

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.no_of_employee} sized {self.company_name} is  {self.raise_amount}")


emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.company_name = "Apple India"  # instance variable
emp1.showDetails()  # if we get instance variable then it will assign that otherwise it will assign class variable
# Employee.showDetails(emp1)  # -> this is another way to call the function

emp1 = Employee("Rohan")
emp1.showDetails()
