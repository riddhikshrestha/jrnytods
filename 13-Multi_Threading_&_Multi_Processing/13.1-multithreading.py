## Multithreading
# When to use Multi Threading
##1. I/O-bound task: Tasks that spend more time waiting for I/O operation (e.g., file operation, network requests).
##2. Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.


import threading
import time

def print_numbers():
    for i in range(5):
        ## Make sleep for 2 second
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# t=time.time()
# print_numbers()
# print_letter()
# finished_time=time.time()-t
# print(finished_time)

### Here we create a single thread.
## Multithreading  - concurrent execution - parallel thread execution

## create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t= time.time()
## start the thread
t1.start()
t2.start()
## wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)