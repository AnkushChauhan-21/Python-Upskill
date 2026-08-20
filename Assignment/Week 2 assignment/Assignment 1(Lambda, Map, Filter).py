# Task 1 
print("\n---- Task 1 ------\n")

a = [1 , 2 , 3 , 4 , 5]
print(f"The Original values : ",a)
double_value = list(map(lambda x:x*2 , a))
print("The Double value is : ",double_value)



# Task 2 
print("\n----- Task 2 -----\n")

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 8 , 9 , 10]
even_numbers = list(filter(lambda x:x%2 == 0,numbers))
print("The Original number list is : ",numbers)
print("The List with filter even numbers only : ",even_numbers)



# Task 3

print("\n----- Task 3 ------\n")
from functools import reduce
words = ["apple" , "small" , "caretoexplain" , "Master" , "Administration"]
longest_word = str(reduce(lambda x,y: x if len(x)>=len(y) else y ,words))
print("The orignal words list is : ",words)
print("The longest word is : ",longest_word)



# Task 4 

print("\n------ Task 4 ------\n")
floats = [2.34 , 4.567 , 3.45 , 4.6 , 9.6]
square_and_round = list(map(lambda x: round(x**2,1),floats))
print("The Original floats list is here : ",floats)
print("The square and round off floats are here : ",square_and_round)


# Task 5

print("\n----- Task 5 ---------\n")
names = ["Rohaan" , "vegetaa" , "Gordonram" , "Super minion" , "Goku" , "Akeno"]
small = list(filter(lambda x: len(x)<=7,names))
print("The Original List is : ",names)
print("The Small name in the whole list is : ",small)


# Task 6

print("\n------ Task 6 -----\n")
num = [1 , 2 , 3 , 4 , 5 , 6]
sum = int(reduce(lambda x,y : x+y , num))
print("The Original Num list : ",num)
print("The sum is : ",sum)





