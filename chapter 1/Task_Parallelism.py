from concurrent.futures import ThreadPoolExecutor
import time

def task_1():
    # Perform addition of two numbers
    result = 5 + 3
    print("Task 1 is executed: 5 + 3 =", result)
    return result

def task_2():
    # Perform subtraction of two numbers
    result = 10 - 4
    print("Task 2 is executed: 10 - 4 =", result)
    return result

start_time = time.time()  # Start timing

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)
    future2 = executor.submit(task_2)

    # Wait for the tasks to complete and retrieve results
    result1 = future1.result()
    result2 = future2.result()

end_time = time.time()  # End timing
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
