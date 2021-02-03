class pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class myeditor:

    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = myeditor()
# ide = pycharm()

lap1 = Laptop()
lap1.code(ide)   # ide object is of myeditor type which is sent as argument in class laptop
