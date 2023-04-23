class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property  # if we use property decorator, we can use this as a getter || It is also a process of encapsulation
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter  # if we use __func__.setter, we can update the value
    def ten_value(self, new_value):  # method name have to be same
        self._value = new_value / 10


obj = MyClass(10)  # this we use for getter method @property
print(obj.ten_value)

obj.ten_value = 67  # this we use for setter method @property
print(obj.ten_value)
obj.show()
