# Min and Max functions
# min() : Returns the smallest item in an iterable or the smallest of two or more arguments
# max() : Returns the largest item in an iterable or the largest of two or more arguments
# Works with tuple,dict,number,list,strings and  other comparable data types
# Syntax : min(iterable, *[,default=obj , key=function]) or min(arg1,arg2,args[,key=function]) 

print("\n-- lets print the min and max with a list of numbers----")
num = [1,2,3,4,5,67,8,9,0]
print("The Original list : ",num)
print("The minimum value in the list by int value : ",min(num))
print("The maximum  value in the list by int value : ",max(num))


print("\n--- lets print the min and max value based on the string unicode value here----\n")
fruits = ["apple" , "banana" , "cherry" ,"date"]
print("The Original fruits list is : ",fruits)
print("The minimum value in the fruits or string is : ",min(fruits))  # "apple" has the min  unicode value
print("The maximum value in the fruits or string is : ", max(fruits)) # "dates" has the max unicode value


print("The minimum value in the : ",min("jasdhfgahsdhUEhHKHFHjkshdhafhhfhfhj"))
print("The minimum value in the : ",max("jasdhfgahsdhUEhHKHFHjkshdhafhhfhfhj"))


print("\n--- Lets print the min and max value of the string using their length\n")
# we will use the previous fruits string list
print("The Min value based on the lenght is : ",min(fruits,key= len))
print("The Max value based on the lenght is : ",max(fruits,key= len))


print("---\n Lets use the min and max with the dictionaries and see what happens\n--")
fru = {
    "apple" : 3,
    "mango" : 1,
    "banana" : 0.9
}

print("The min value in the fru is : ",min(fru))
print("The max value in the fru is : ",max(fru))
print("min value based on the key of fru : ",min(fru.keys()))
print("max value based on the key of fru : ",max(fru.keys()))
print("min value based on the values of fru : ",min(fru.values()))
print("max value based on the values of fru : ",max(fru.values()))
print("min value based on the key: value pair now : ",min(fru.items()))
print("max value based on the key:value pair now :",max(fru.items()))



# Using the min and max with tuple
# Tuples are comapred element by element
# (x1 , y1) > ( x2 , y2)
# if x1 > x2 then (x1 , y1) > ( x2 , y2)
# if x1 == x2 then y1 and y2 are compared

tuple1 = (1 , 2 , 3)
tuple2 = (3 , 4 , 6)
print("\n-- lets print and use min and max with the tuple-----\n")
print("tuple1 : ",tuple1)
print("tuple2 : ",tuple2)
# Lets use the min and max now on this tuple
print("The tuple with the min value is : ",min(tuple1,tuple2))
print("The tuple with the max value is : ",max(tuple1,tuple2))


# lets print the the empty tuple or list and give it a default value so that it will not throw the error
empty = []      
print("The min value of this empty list is : ",min(empty,default= "This is the empty list"))
print("The max value of this empty list is : ",max(empty,default= "This is the empty list"))



# Lets print the min and max using a list based on the index we desire
demo = ["apple" , "banana" , "tomato" , "kiwi" , "cherry"]
print("The original list is : ",demo)
print("The min value based on the index is : ",min(demo,key= lambda x: x[-1]))
print("The max value based on the index is : ",max(demo,key= lambda x: x[-1]))



print("\n")
int_string = ["11" , "34" , "1" , "6" , "1"]
print("\n The original list is : ",int_string)
print("\n The min vale is " ,min(int_string,key=int))
print("\n The max vale is " ,max(int_string,key=int))




