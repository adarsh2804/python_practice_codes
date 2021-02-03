# Method Resolution Order:- In multiple inheritance calling is always from left to right


class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 in A working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature 1 in B working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()   # this will call init of A class as it will go from left to right
        print("In C init")

    def feat(self):
        super().feature2()


a1 = C()                              # this constructor will call init of C class
a1.feature1()   # it will call the feature1 of A class as it goes from left to right therefore B class is not called
a1.feat()
