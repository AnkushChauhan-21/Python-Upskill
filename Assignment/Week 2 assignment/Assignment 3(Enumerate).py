# Task 1 
print("\n---- Task 1 -----\n")
fruits = ["apple" , "mango" , "grapes"]
for index , fruit in enumerate(fruits):
    print(f" {index} : {fruit}")


# Task 2 
print("\n---- Task 2 ----\n")
person = { "Name" : "Ankush" ,
           "Age" : 21 ,
           "gender" : "Male"

          }

for index ,(key,value) in enumerate(person.items()):
    print(f"{index} : ({key,value})")


print("\n----- Task 3 -------\n")
fruitss = ["apple" , "mango" , "grapes" , "banana"]
fruit_tuple = []
for index , fru in enumerate(fruitss):
    if(index%2==0):
        fruit_tuple.append((index,fru))
print(f"The index are as follow {fruit_tuple}")


