class Parent:                           # parent/super class

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class Child(Parent):                   # child/sub class inherited from parent class

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class Grandchild(Child):               # inherited from child class :- multilevel inheritance

    def feature5(self):
        print("Feature 5 working")


p1 = Parent()                          # object of super class
p1.feature1()                          # can access methods/variables of parent class only
p1.feature2()

c1 = Child()                           # object of sub class
c1.feature1()                          # can access methods/variables of both parent and child class
c1.feature3()

gc1 = Grandchild()                     # object of grandchild class
gc1.feature4()                         # can access methods/variables of all parent, child and grandchild class
gc1.feature2()
gc1.feature5()
