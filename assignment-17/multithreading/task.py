import multiprocessing

def prnt_cu(n):

    print("Cube: {}".format(n * n * n))

def prnt_squ(n):

    print("Square: {}".format(n * n))

if __name__ == "__main__":

# creating multiple processes

    proc1 = multiprocessing.Process(target=prnt_squ, args=(5, ))

    proc2 = multiprocessing.Process(target=prnt_cu, args=(5, ))

# Initiating process 1

    proc1.start()

    # Initiating process 2

    proc2.start()

    # Waiting until proc1 finishes

    proc1.join()

    # Waiting until proc2 finishes

    proc2.join()

    # Processes finished

    print("Both Processes Completed!")