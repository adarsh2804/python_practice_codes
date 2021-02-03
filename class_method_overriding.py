class A:

    def show(self):
        print("in A show")


class B(A):

    def show(self):            # If child and parent both has method with same name, method of child will
        print("in B show")     # override the method of parent


a1 = A()
a1.show()

b1 = B()
b1.show()  # this will call show method of B class as it will override show method of A class
