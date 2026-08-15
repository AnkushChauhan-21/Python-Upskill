# Decorators in python
# Decorators are special function that modifies the behaviour of the another function
# Decorators allow you to wrap another function to extend its 
# behaviour without modifying its content

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("something is happening before the function")
        func(*args,**kwargs)
        print("something is happening after the function")
    return wrapper


def say_hello():
    print("hey its me goku")



say_hello()

# wrapper is used becaused without it, the decorator will execute at the place it is defined,not when the decorator function is called
#  you can also create the decorator that accept the arguments 


# Example of decorator with the arguments
def time_to_repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args , **kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return decorator_repeat

@time_to_repeat(num_times=3)
def the_power(power):
    print(f"What he has the power level of {power} !!!!!!!!!")


the_power("3000")


# In this example , the the_power function will print the our message with the power level three times because of our time_to_repeat decorator that we created here
# Decorators are widely used  in python for logging, access control,instrumentation , and caching , among other things
# you can also use the  built-in decorators  like @staticmethod, @classmethod , and @property in classes.

#Multiple decorators can be applied to a single function as well

def upper_case(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

@my_decorator
@upper_case
def name_upp(name):
    print(f"Your name in Capitalize is {name.upper()}")

name_upp("ankush")

# In this above function first num_upp result is given to the @upper_case then its result goes to the @my decorator
# The Order of the decorators matter : They are applied from the bottom to up
# Note : The decorator can also be applied to function with parameters using the *args and **kwargs in wrapper function

def debug_decor(func):
    def wrapper(*args , **kwargs):
        print(f"function {func.__name__} called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args , **kwargs)
        print(f"The function {func.__name__} returned {result} ")
        return result
    return wrapper

@debug_decor
def add(a,b):
    return a+b



print(add(2,3))

# This debug_decor will log the function name, its arguments, and the return value each time the add function is called.