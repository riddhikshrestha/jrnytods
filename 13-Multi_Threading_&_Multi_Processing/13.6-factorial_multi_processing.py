'''
Real world Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculaton
        - Factorial calculaiton, especially for large numbers,
        involve significant computational work. Multiprocessing can be used to distribbute the 
        workload across multiple CPU cores, improving performance.
'''
import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time=time.time()
    #create a pool of workder processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds.")