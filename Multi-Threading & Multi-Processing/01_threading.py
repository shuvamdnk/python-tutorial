from threading import Thread
import time


def take_order():
    for i in range(1,5):
        print("Taking order from customer", i)
        time.sleep(1)

def prepare_food():
    for i in range(1,5):
        print("Preparing food for customer", i)
        time.sleep(4)

# create Threads
t1 = Thread(target=take_order)
t2 = Thread(target=prepare_food)

# start Threads
t1.start()
t2.start()

# wait for Threads to finish
t1.join()   
t2.join()

print("All orders are ready")