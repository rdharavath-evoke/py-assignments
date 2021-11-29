############ By extending Thread class ############

from threading import *
import threading

class A(threading.Thread):
    def run(self):
        for x in range(4):
            print("child",current_thread().getName())
obj=A()
obj.start()
obj.join()
print("control returned to", current_thread().getName())