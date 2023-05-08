# Example -> single inheritance + multiple inheritance

class BassClass:
    pass


class Derived1(BassClass):
    pass


class Derived2(BassClass):  # single inheritance
    pass


class Derived3(Derived1, Derived2):  # multiple inheritance
    pass
