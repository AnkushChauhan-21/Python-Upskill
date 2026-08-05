# function = its a block of code that runs only when it is called. we can pass data , known as parameters, into the function. A function can return data as a result.

def birthday_wishes(name):
    print(F"happy birthday dear {name}!!!")
    print("may you live a happy and very long life again this year",end="\n\n")

birthday_wishes("Ankush")
birthday_wishes("rohan")
print(birthday_wishes("ankush"))   # this will print none  because function does not have anything to return
print(birthday_wishes,end="\n\n")   # this will print the function object location.



# function with the return value
print("\n--- function with the return value here---")

def number(num1,num2):
    return num1 + num2
result = number(4,6)
print(f"the sum of the two nuumber is {result}",end="\n")




# function with the default parameters 
print("\n--- printing the function with the default parameter---")
def greeting(name,message="konnichiwa"):
    print(f"hello Master {name} , {message}")

greeting("ankush")  # this will  give ankush as name but default konichiwa as message 
greeting("Ankush" , "goodmorning to you") # This will give ankush as the name and the message will be good morning as we already gave it in parameter so there is no need for the default one to run 



# function with variable number of arguments
def multi(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(f"multiplication results are : {multi(2,3,6,7,10)}",end="\n")
print(f"multiplication results are : {multi(10,10,2)}",end="\n")


# lamba function (Anonymus function)
sqaure = lambda x:x * x 
print(f"the sqaure of {sqaure(5)}")
print(f"the sqaure of {sqaure(6)}")
print(f"the sqaure of {sqaure(12)}")


# Nested functions here with an example
def outer_function(text):
    def inner_function():
        return text.upper()
        return inner_function()
print(outer_function("hello world i am a pyhton code"))
print(outer_function("world"),end = '\n\n')# this will print hello world in upper case


#Recursive function here with an example
print("\n---printing the recursive function here---")
n = int(input("enter the number to find the factorialof it here :  "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(f"the factorial of {n} is {factorial(n)}")
print(f"the factorial of {n}  is {factorial(n)},end = '\n\n'")


# function annotation
def greet(name:str) -> str:
    return f"Hello Dear ,{name} how are you doing today???^_^"
print(greet("Ankush"))
print(greet("Rohan"),end = '\n\n')


# Higher order function
print("\n-- printing the higher order function here---")
# This function takes another function as an argument and returns a new function as a result.
def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x * 2, 5))
print(apply_function(lambda  x: x + 10, 5), end = '\n\n')



# keywords arguments here with an example
print("\n--- printing the keyword argunments here---")

def student_details(name,age,grade):
    print(f"Mr/Mrs {name} is {age} years old and he/she is in grade {grade}")
student_details(name='Ankush',age = 21 , grade = "A")
student_details(name='Ankur',age = 23 , grade = "B")



# Lets try the doc string with an example here
def add_numbers(a,b):
    #this function takes two numbers as input and returns their sum>
    return a + b
print(add_numbers(5,0))
print(add_numbers.__doc__) # this will print the doc string of the function add_numbers
print(add_numbers,end = '\n\n') # this will print the function object location


# variable scope with an example here
x = 10  # global variable 
def modify_variable():
    global x # this will tell the function to use the global variable x instead of creating a new local variable with the same name 
    x = 20 # this will modify the global variable x to 20
    print(f"inside the function the value of x is , x = {x}") 
modify_variable()               
print(f"outside the function the value of x is , x = {x}")

# lets talk about kwargs and args with an example here
# *args = it allows a function to accept any number of positional arguments as a tuple.
# *kwargs = it allows a function to accept any number of keyword arguments as a dictionary
# positonal arguments = these are the arguments that are passed to a function in a specific order. The order of the arguments matters and they are assigned to the parameters in the same oder as they are passed.
# keywords arguments = arguments that are passed to a function by explicitly naming each parameter and its corresponding value.
print("\n--- printing the args and kwargs here---")
def fun_with_args_kwargs(*args, **kwargs):
    print("positional arguments args: ", args)
    print("keyword arguments kwargs: ", kwargs, end = '\n\n')

fun_with_args_kwargs('a' , 'b', key1 = "value1" , key2 = "value2")
fun_with_args_kwargs(1,2,3, name  = "Ankush" , age  = 21)


course = [ "C++" , "DSA" , "Log" ,"time complexity"]
info = {
    "name" : "Ankush",
    "age"  : 21 ,
    "grade" : "A" 

}

fun_with_args_kwargs(*course , **info)