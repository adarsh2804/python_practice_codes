class Student:

    school = 'Prestige'                 # class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1                    # instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):                      # instance method:- works with instance variable
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):                   # accessor method:- only access cant modify
        return self.m1

    def set_m1(self, value):            # mutator method :- can access and modify value
        self.m1 = value

    @classmethod                        # decorator
    def getschool(cls):                 # class method:- works with class variable
        return cls.school

    @staticmethod                       # decorator
    def info():                         # static method:- no parameter
        print("This is student class static method")


s1 = Student(34, 86, 36)
s2 = Student(98, 65, 24)

print(s1.avg())
print(Student.getschool())
Student.info()
