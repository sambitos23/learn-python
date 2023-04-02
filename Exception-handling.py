a = input("Enter the number: ")
print(f"multiplication table of {a}")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
# except Exception as e:
#     print(e)
except:
    print("Invalid Input", type(a))

print("Some imp line of code")


try:
    num = int(input("Enter a integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index error")
