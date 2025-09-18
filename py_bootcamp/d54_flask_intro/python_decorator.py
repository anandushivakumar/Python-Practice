import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        time_diff = end_time - start_time
        print(f"{func} run speed: {time_diff}")
    
    return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i # type: ignore
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i # type: ignore

fast_function()
slow_function()