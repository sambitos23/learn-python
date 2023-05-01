class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod  # don't add to add self
    def add(num1, num2):
        return num1 + num2


result = Math.add(1, 2)
print(result)

print("=========================")

a = Math(5)
print(a.num)
a.add_to_num(6)
print(a.num)
