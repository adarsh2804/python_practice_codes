class Student:

    def __init__(self, name, rollno):      # outer class function
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()           # calling the inner class by self.lap

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()                    # calling show() of inner class by self.lap

    class Laptop:            # inner class

        def __init__(self):
            self.brand = 'Asus'            # inner class variables
            self.cpu = 'i5'
            self.ram = 16

        def show(self):                    # inner class function
            print(self.brand, self.cpu, self.ram)


s1 = Student('Adarsh', 5)    # object of outer class
s2 = Student('Koustubh', 50)

s1.show()                    # will call show() of outer class as s1 is object of outer class

# s1.lap.brand
lap1 = s1.lap                # object of inner class
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

lap1.show()                  # will call show() of inner class as object is of inner class
