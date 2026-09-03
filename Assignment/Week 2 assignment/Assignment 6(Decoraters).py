# Task 1
import time
print("\n------ Task 1 ------\n")
lists = []


def calculate_the_performance(func):
    def wrapper():
        start_time = time.time()
        print("The start time is executing here : ",start_time)
        func()
        end_time = time.time()
        print("The end time is executing here : ",end_time)
        print("The total time taken in appending the list : {:.6f}seconds".format(end_time - start_time))
    return wrapper



@calculate_the_performance
def func_to_append():
    for i in range(1,1000):
        lists.append(i)

func_to_append()






# Task 2 
print("\n------ Task 2 ------\n")


def retry(num_times):
    def repeat(func):
        def wrapper(*args ,**kwargs):
            for i in range(0,num_times):
                func(*args , **kwargs)
        return wrapper
    return repeat    




@retry(4)
def repeat_this(name):
    print(f"welcome Master {name}!")

repeat_this("Ankush")



# Task 3
print("\n------ Task 3 ------\n")

def validating_the_positive(func):
    def wrapper(*args , **kwargs):
        if(all(arg>0 for arg in args)):
            return func(*args , **kwargs)
        else:
            print("This number is not a positive number,Please enter a positive number here")
    return wrapper

def sqr_root(x):
    return x**0.5

print(int(sqr_root(144)))



# Task 4
print("\n------ Task 4 ------\n")


        
