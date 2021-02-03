from time import sleep
from threading import *


class Hello(Thread):            # inherited from the thread class
    def run(self):              # method name must be run as it is already define in the thread class
        for i in range(5):
            print("Adarsh")
            sleep(1)            # will take pause of 1 second


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Shrivastava")
            sleep(1)            # pause is given to be clear about gap in printing output by 2 processors


t1 = Hello()
t2 = Hi()

t1.start()             # this will call the run method of class hello by default
sleep(0.2)             # pause is given to avoid the collision at CPU
t2.start()

t1.join()              # it will let the job of t1 be finished alongwith t2 first, then bye will be printed at the end
t2.join()

print("Bye")
