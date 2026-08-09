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


# Task 3
print("\n----- Task 3 -------\n")
sqr_nums =[n*n for n in range(1,6)]
print("The square of the numbers in the range are : ",sqr_nums)



# Task 4 
print("\n----- Task 4 -----\n")
matrix = [[1,2,3] , [6,-7,8] , [2,3,5]]
flat_list = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
print("The First variable is : ",matrix)
print("The flat_list is : ",flat_list)




# Task 5
print("\n---- Task 5 -----\n")
name = ["ankush" , "raven" , "tarun"]
age = [ 23 , 34 , 31]
dict_way = { key : value for key ,value in zip(name , age)}
print("lets print the key and value pairs in the dict_comp  : ",dict_way) 



# 