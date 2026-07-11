#Mutablitiy of the list
print("\n---Mutability of the list---")
list1 = ["rohan" , "mayank" , "kumar" , 'Seema']
list2 = list1
print("\n original list here : ",list1)
print("\n original list2 (refernce the list 1)" , list2)


# modifying the list and checking the output here
print("\n-- modifying the list here and printing the output--")

list2[0] = "modified"
print("printing the modified list2 here : " ,list2)
print("printing the modified list1 here : " ,list1)  # as we can see the list1 is also modified like list 2 means the list is mutable in nature 


#lets do same with tuple 

print("\n--tuple--")

tuple1 = ("monthly","weekly","daily","hourly")
tuple2 = tuple1
print("the output of the tuple1 is : ",tuple1)
print("the output of the tuple2 (referencing the tuple1) is : ",tuple2)


# lets try to modify it and see what output we get here
tuple2[0] = "modified"
print("\n the output of the tuple2 after modifying it here :  ",tuple2)
print("\n the output of the tuple1  :  ",tuple1)

# Tuple is immutable in nature we can modified it as it will throw the 
# TypeError: 'tuple' object does not support item assignment
