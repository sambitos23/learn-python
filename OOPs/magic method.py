class Employee:
    name = "Sambit"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i

    def __str__(self):
        return f"The name of the employee {self.name} str"

    def __repr__(self):  # represent object ka tarika jiss us object ko create kiya ja sakta hai
        return f"Employee('{self.name}')"

    def __call__(self, *args, **kwargs):
        print("Hey I am call")


e = Employee()
print(e.name)
print(len(e))

print(e)
print(str(e))
print(repr(e))
e()  # callback function __call__
