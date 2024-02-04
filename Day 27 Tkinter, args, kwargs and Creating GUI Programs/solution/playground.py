def add(*args):
    return sum(args)


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GTR")
print(my_car.model)
calculate(2, add=3, multiply=5)

total = add(4, 5, 6)
print(total)


