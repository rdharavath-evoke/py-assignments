
import threading
import multiprocessing


def file1(n):
    
    f = open(r'C:\Users\rdharavath\Documents\thread1.txt')
    print(f.read())
        
def file2(n):
    f = open(r'C:\Users\rdharavath\Documents\thread2.txt')
    print(f.read())
    
def file3(n):
    f = open(r'C:\Users\rdharavath\Documents\thread3.txt')
    print(f.read())
    
def file4(n):
    f = open(r'C:\Users\rdharavath\Documents\thread4.txt')
    print(f.read())

if __name__ == "__main__":

# creating multiple processes
    n=int(input("Enter no. of files to read and print: "))
    for i in range(1,n+1):
        if i==1:
            proc1 = multiprocessing.Process(target=file1,args=(n,))
            proc1.start()
        elif i==2:
            proc2 = multiprocessing.Process(target=file2,args=(n,))
            proc2.start()
            proc2.join()
        elif i==3:
            proc3 = multiprocessing.Process(target=file3,args=(n,))
            proc3.start()
            proc3.join()
        elif i==4:
            proc4 = multiprocessing.Process(target=file4,args=(n,))
            proc4.start()
            proc4.join()

    # Initiating process 1

    # proc1.start()

    # # Initiating process 2

    # proc2.start()

    # # Initiating process 3

    # proc3.start()
    
    # # Initiating process 4

    # proc4.start()

    # # Waiting until proc1 finishes

    # proc1.join()

    # # Waiting until proc2 finishes

    # proc2.join()

    # # Processes finished
    
    # proc3.join()

    # # Processes finished
    # proc4.join()

    # # Processes finished

    print("all Processes Completed!")