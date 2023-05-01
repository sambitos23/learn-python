class Employee:
    company = "Apple"

    def show(self):
        print(f"The name of the Employee is {self.name} and company is {self.company}")

    @classmethod
    def change_company(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Sambit"
e1.show()
e1.change_company("Tesla")
e1.show()
print(Employee.company)