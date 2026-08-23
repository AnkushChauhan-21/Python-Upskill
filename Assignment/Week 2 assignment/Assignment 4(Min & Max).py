# Task 1
print("\n----- Task 1 ------\n")
numbers = [1,2,3,5,6,7,8,5,42,1,24,543,2,56]
print(f"The Orignal list of numbers is : {numbers}")
print("minimum value in the list is : ",min(numbers))
print("maximum value in the list is : ",max(numbers))


print("\n----- Task 2 -----\n")
setn = {1,2,4,5,7,8,5,34,67,8,9,34524,2}
print("The Original set is : ",setn)
print("The max value is : ",max(setn))
print("The min value is : ", min(setn))


print("\n------- Task 3 --------\n")
words = ["apple" , "mango" , "dynamite" , "beautiful"]
print("The Original list is : ",words)
output = (min(words , key=len) , max(words , key=len))
print("The min and max of the words are : ",output)