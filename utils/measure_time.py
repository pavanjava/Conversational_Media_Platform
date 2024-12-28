import time
from functools import wraps

def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Record the start time
        result = func(*args, **kwargs)   # Call the original function
        end_time = time.perf_counter()   # Record the end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper