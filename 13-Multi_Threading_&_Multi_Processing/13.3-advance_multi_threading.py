## Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,4,6,7]

with ThreadPoolExecutor(max_workers=3) as executor:     #much more lossly coupled
    results=executor.map(print_numbers,numbers)

for result in results:
    print(result)