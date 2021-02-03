class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):     # it is overloading (+) operator between s1 and s2 objects
        m1 = self.m1 + other.m1   # if not overloaded s1 + s2 will give error as they are objects not integer
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)

        return m3

    def __gt__(self, other):      # it is overloading (>) operator between s1 and s2 objects
        r1 = self.m1 + self.m2    # if mot overloaded s1>s2 will give error as objects cant be compared like integers
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):            # it is overloading (print) operator of s1 and s2 objects to give their values
        return '{} {} '.format(self.m1, self.m2)


s1 = Student(66, 97)
s2 = Student(45, 76)

s3 = s1 + s2            # this will call the add method in student class
print(s3.m1, s3.m2)

if s1 > s2:             # this will call the gt method in student class
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a.__str__())

print(s1)               # this will call the str method in student class
print(s2)               # if str method doesnt overload print, it will give address of object s2
