class Computer:

    def config(self):
        print("i5, 16gb, 1TB")


a = 5
print(type(a))

b = 'adarsh'
print(type(b))

com1 = Computer()
com2 = Computer()
print(type(com1))

Computer.config(com1)
Computer.config(com2)

com1.config()  # com1 is object passed as parameter self of config method
com2.config()
