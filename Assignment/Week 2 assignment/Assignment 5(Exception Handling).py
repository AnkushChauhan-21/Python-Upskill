# Task 1
print("\n----- Task 1 -----\n")
try:

    a = 10
    b = 0
    result = a/b
    print(f"The result is {result}")
except ZeroDivisionError as Error:
    print(f"The result is the {Error}")



# Task 2
print("\n------- Task 2 -----\n")
list = [1,2,3]
try:

    print(list[5])
except IndexError as ie:
    print(f"The Error is {ie}")

# Task 3 
print("\n------- Task 3---------\n")
def take_input(a,b):
    try:
        result1=a/b
    except ZeroDivisionError as ze:
        print(f"The Error is {ze}")
    except TypeError as typ:
        print(f"The error is {typ}")
    else:
        print(f"The result is {result1}")
   

try:

   take_input(1,0)
   take_input(1,"a")
finally:
    print("The execution is done here")
