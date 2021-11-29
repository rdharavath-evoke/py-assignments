############ without creating a class #########

from threading import *
def new():
    for x in range(6):
        print("child Executing....", current_thread().getName())
t1=Thread(target=new)
print(current_thread().getName())
t1.start()
t1.join()
print("done->", current_thread().getName())