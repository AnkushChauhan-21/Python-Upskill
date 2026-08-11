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

