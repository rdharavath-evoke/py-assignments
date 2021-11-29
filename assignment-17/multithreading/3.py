######## without extending the thread class #######

from threading import *

class Example:
    def myfunc(self):
        for x in range(5):
            print("Child printing")
myobj=Example()
thread1=Thread(target=myobj.myfunc)
thread1.start()
thread1.join()
print("done")