# method overloading is not supported in python therefore we can implement following code instead


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):         # by default value of the parameters will be none

        s = 0

        if a != None and b != None and c != None:  # if all 3 values are passed as argument
            s = a + b + c
        elif a != None and b != None:              # if only 2 values are passed as argument
            s = a + b
        else:
            s = a                                  # if only 1 value is passed as argument

        return s


s1 = Student(66, 97)

print(s1.sum(5, 6))     # it will pass value in sum method which by default has none value
