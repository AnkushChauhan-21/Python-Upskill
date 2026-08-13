# Decorators in python
# Decorators are special function that modifies the behaviour of the another function
# Decorators allow you to wrap another function to extend its 
# behaviour without modifying its content

def my_decorator(func):
    def wrapper():
        print("something is happening before the function")
        func()
        print("something is happening after the function")
    return wrapper


def say_hello():
    print("hey its me goku")



say_hello()
