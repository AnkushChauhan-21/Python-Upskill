# all and any functions
# all() : Returns True if all the elements in the iterables are True,(or if the iterable is empty) 
# any() : Returns True if any element in the iterable is True ,  but return False if the iterable is empty


boolean = [True,False,True,False]
string = ["" ,"Money","honey" ]
numbersss = [0,1,2,3]

# lets test and see the all() and any() on boolean list
print("\n The Original List : ",boolean)
print("All elements are True : ",all(boolean))
print("At least one element is True : ",any(boolean))



# lets try all() and any() on num list
print("\n The Original List : ",numbersss)
print("All elements are non-zero : ",all(numbersss))
print("At least one element is non-zero  : ",any(numbersss))


# Lets try all() and any() on string list
print("\n The Original List : ",string)
print("All strings are non-empty : ",all(string))
print("At least one string is non empty : ",any(string))


#Useful when used with logical Conditions
ages = [0, 25, 18, 30, 27]
print(ages)
print("All age are above 25 : " ,all(age >= 18  for age in ages))
print("At least one is above 25 : ",any(age >=25 for age in ages))

# Numpy Examples
import numpy as np
array = np.array([[1,2,3] , [3,45,6] , [2,4,5]])
print("The Original Array is : ",array)
print("All elements in the array are non-zero : ",np.all(array))
print("At least one element in the array is non-zero : ",np.any(array))


# Lets Take the example of the power levels 
power_level = np.array([6000,4500,7000,45000,9000,10000])
print("The Original Array is : ",power_level)
print("All power levels exceed 8000 : ",np.all(power_level > 8000))
print("At least one power level exeed 9000 : ",np.any(power_level > 9000))


# Enumerate function
# The enumerate() function adds an counter to an iterable and return it as the enumerate  object
# Syntax : enumerate(iterable,start=0)

print("\n---- lets print the enumerate function here ----")
fruits = ["Apple" , "mango" , "banana"]

for index , fruit in enumerate(fruits):
    print(f"Index {index} : {fruit}")



new_index = ["Apple" , "mango" , "banana"]
for index , fruit in enumerate(new_index, start=1):
    print(f"\n Index {index} : {fruit}")






