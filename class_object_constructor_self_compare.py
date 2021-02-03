class Computer:

    def __init__(self):
        self.name = 'adarsh'
        self.age = 24

    def update(self):
        self.age = 25

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
print(id(c1))
# c1.age = 24
c2 = Computer()
print(id(c2))

c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)
