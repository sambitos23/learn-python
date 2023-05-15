a = input("Enter a value between 5 and 9: ")


class QuitError(Exception):
    pass


if a != 'quit':
    raise QuitError("Value is an string")
if int(a) < 5 or int(a) > 9:
    raise ValueError("Value should be between 5 and 9")
