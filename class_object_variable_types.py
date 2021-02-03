
class Car:

    wheels = 4                # class/static variable:- changes value of all objects

    def __init__(self):
        self.mil = 10         # instance variable:- particular to an object
        self.comp = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
