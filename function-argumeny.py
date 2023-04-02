def avg(a=9, b=1):  # default argument
    print("The avg is ", (a + b) / 2)


avg(1, 5)
avg(b=9)


# variable length argument
def average(*numbers):  # * => will take as tuple
    sum = 0
    print(type(numbers))  # tuple
    for i in numbers:
        sum = sum + i
    print("Average is ", sum / len(numbers))


average(5, 6, 4)


def name(**name):  # ** => will take as dict
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(fname="Swapan", mname="Kumar", lname="Saha")
