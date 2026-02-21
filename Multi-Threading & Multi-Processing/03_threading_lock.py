# import threading
# import time

# lock = threading.Lock()  # Create a lock object

# counter = 0  # Shared counter variable

# def increment(lock):
#     global counter
#     for _ in range(100000):
#         with lock:
#             counter += 1

# threads = [threading.Thread(target=increment, args=(lock,)) for _ in range(5)]

# [thread.start() for thread in threads]
# [thread.join() for thread in threads]

# print(f'Final counter value: {counter}')


import threading
import time

lock = threading.Lock()  # Create a lock object

counter = [0] # Shared counter variable

def increment(counter, lock):
    # global counter
    for _ in range(100000):
        with lock:
            counter[0] += 1
    print(f'Counter value in thread: {id(counter)} {counter[0]} {threading.current_thread().name}')        

threads = [threading.Thread(target=increment, args=(counter, lock)) for _ in range(5)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]

print(f'Final counter value: {counter[0]} {id(counter)}')