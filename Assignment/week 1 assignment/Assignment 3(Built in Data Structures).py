print("\n---- Task 1-----\n")
numbers = [1,2,3,4,5,6]
print("maximum number is : ",max(numbers))
print("minimum number is : ",min(numbers))



print("\n--- Task 2 ----\n")
a = [1,2,3,4]
b = [5,6,7,8]
print("a: ",a)
print("b: ",b)
a.extend(b)
print("a extends b will be : ",a)



print("\n----Task 3-----\n")
list = [1,2,3,4,4,5,6,4,5,6,8,4,4,4]
print("lets count the values of all the 4 in our list : ",list.count(4))



print("\n---- Task 4 ----\n")
a = [89,32,67,2,4,7,25,849]
print("the original list is here : ",a)
a.sort()
print("the sorted list will print now here : ",a)


print("\n")
b = [89,32,67,2,4,7,25,849]
b.sort(reverse=True)
print("lets see the reverse sorted list here : ",b)



print("\n--- Task 5 -----\n")
set = {1,3,5,3,4,6,7}
print("The Original set is here : ",set )
set.add(100)
print("Lets See the New set here : ",set)



print("\n--- Task 6 ----\n")
sett = {1,3,5,7,4788,9,89,0,-1}
print("The original sett is : ",sett)
sett.remove(4788)
print("The new Sett After Removing the 4788 is : ",sett)





print("\n---- Task 7----")
set1 = {1,3,5,66,7,7,8}
set2 = {1,7,8,4,3,7,9,66,78,23,7,4}
print("Lets do the set1 intersection with set2 is : ",set1.intersection(set2))

print("\n--- Task 8---\n")
fruits = ("apple","mango","banana","Mango","apple")
print("Lets Count the number of apples in out fruit variable : ",fruits.count("apple"))


print("\n-----Task 9----\n")
tuple1 = (2,3,5,6,7)
tuple2 = (3,5,78,94,24)
tuple3 = tuple1 + tuple2
print("tuple1 : ",tuple1)
print("tuple2 : ",tuple2)
print("tuple3 : ",tuple3)

print("\n-----Task 10----\n")
dict = {
    "Name" : "Ankush" ,
    "age"  :  21  ,
    "city" :  "Delhi"
}
print("lets print the whole dict : ",dict)
print("lets get the value of the age : ",dict.get("age"))
print("lets get the value of the age : ",dict["age"])
print("lets get the value of the city : ",dict["city"])



print("\n-----Task 11----\n")
dict = {
    "Name" : "Ankush" ,
    "age"  :  21  ,
    "city" :  "Delhi"
}

print("lets add and update this dict : ",dict.update({"Gender"  : "Male"}))

print("Lets Print the updated dict now : ",dict)



print("\n-----Task 12----\n")
dict = {
    "Name" : "Ankush" ,
    "age"  :  21  ,
    "city" :  "Delhi"
}

poop = dict.pop("city")
print("lets print the dict now we have poped out the city : ",dict)
print("printing the pop element too side by side : ",poop)
