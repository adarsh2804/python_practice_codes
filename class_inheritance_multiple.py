class Parent:                           

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class Child:

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class Grandchild(Parent, Child):       # inherited from both parent and child class :- multiple inheritance

    def feature5(self):
        print("Feature 5 working")


p1 = Parent()
p1.feature1()

c1 = Child()
c1.feature3()

gc1 = Grandchild()                     # object of grandchild class
gc1.feature4()                         # can access methods/variables of all parent, child and grandchild class
gc1.feature2()
gc1.feature5()
