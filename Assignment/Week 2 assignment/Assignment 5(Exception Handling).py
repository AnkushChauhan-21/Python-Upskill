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

    