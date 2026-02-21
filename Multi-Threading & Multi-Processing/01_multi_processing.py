from multiprocessing import Process
import multiprocessing
import time

def take_order():
    for i in range(1,5):
        print("Taking order from customer", i)
        time.sleep(1)

def prepare_food():
    for i in range(1,5):
        print("Preparing food for customer", i)
        time.sleep(4)

if __name__ == "__main__":

    print(multiprocessing.cpu_count())  # number of CPU cores

    # create Processes
    process_list = []
    for i in range(10):
        p = Process(target=take_order)
        process_list.append(p)

    # p1 = Process(target=take_order) 
    # p2 = Process(target=prepare_food)

    # start Processes
    for p in process_list:
        p.start()


    # wait for Processes to finish
    for p in process_list:
        p.join()

    print("All orders are ready")