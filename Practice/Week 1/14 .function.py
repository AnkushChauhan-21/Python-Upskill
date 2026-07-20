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


print("\n printing for the vs code in the github")


print("\n i hate coffee")