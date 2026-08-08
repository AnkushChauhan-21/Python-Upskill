# Task 1 
print("\n------- Task 1 -----\n")
string = ["1","2","3","4","5"]
nums = [int(n) for n in string]
print("Original string and its type : ",string,type(string))
print("new list and its type  : ",nums ,type(nums))


# Task 2 
print("\n----- Task 2 -------\n")
list = [1,2,3,4,89,454,32,56,3,6,52]
greator_than_10 = [n for n in list if n>10]
print("The Original list is : ",list)
print("The Other list is : ",greator_than_10)