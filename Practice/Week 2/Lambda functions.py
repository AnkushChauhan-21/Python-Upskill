from functools import reduce
 # Lambda functions are anonymous functions that can be used to  create small functions without  a name 
 # They are defined using the lambda keyword
 # They are also known as the anonymous functions
 # They are used to create the small functions without a  name 
 # They are used  when we need to pass a  function as an argument to  other function



 # syntax : lambda arguments: expression
 # Example 1
print("\nlambda function\n")
square=lambda x: x*x
print(square(2))


# Example 2
Add = lambda x,y: x + y
sum = Add(2,7)
print(sum)


# Example 3 
multiply = lambda x,y,z: x*y*z
print(multiply(2,4,6))


# Map function
# The map function is used to apply a function to each item in an iterable
# It returns a new list with the result of the function applied  to each item
# syntax : map(function,iterable)    # iterables : list,dict,tuple,set

# Example of map function
print("\n map function\n")
number= [1,2,3,4,5,6,7,6]
print("The original list is : ",number)
squared = list(map(lambda x: x**2,number))
print("The Square list : ",squared)


# Filter Function
# Filter is used to filter the items in an iterble
# Syntax : filter(function,iterable)
# filter example 

print("\n filter function")
num = [1,2,4,6,7,4,234,67,84689,9876,3]
print("The original list is : ",num)
even =list(filter(lambda x: x % 2 == 0,num))
print("The number is even : ",even)

# Reduce Function
# The reduce function is used to reduce an  iterable to a single value
# In this function the first argument is always the result of the previous function call known as accumulator
# Syntax : (function,iterable)
# Example of the reduce function 

Num = [1,2,3,4,5,6,6,7,8,8,6]
print("The Original list : ",Num)
# without intializing the accumulator
sum = reduce(lambda x,y: x + y,Num)
print(sum)



# with initializing the accumulator
sum2 = reduce(lambda x,y: x + y,Num,10)
print(sum2)
