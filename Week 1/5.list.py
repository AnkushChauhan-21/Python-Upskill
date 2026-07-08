print("\n----list----")
#list is ordered,and it is mutable and it allows duplicate elements collections
list = [1 , 2 , 3 , "hello" , "mango" , 7.5 , 986]
print("Printing my first list here : ",list)


#Accessing the elements using their indexes 
print("\n---accessing the elements using the index--")
print("accessing the first elements of the list : ",list[0])
print("accessing the last elements of the list : ",list[6])


#slicing the elements of list
print("\n---slicing the elements of list---")
print("slicing the elements from 1 to 3 : ",list[0:4]) #4 is exluded so it will print till 0-3 only as first index is inclusive
print("slicing the elements from start to end with steps : ",list[0::2])

#modifying the element as we can modify it because list is mutable means it can be modify easily
print("\n---Modified list---")
list[0] = 4
print("modified list : ",list)


# methods of list 
print("\n---methods of list---")
subjects = ['maths' , 'chemistry' , 'physics' , 'english']
subjects_2 = ['Hindi' , 'Sanskrit' , 'english' , 'maths']
print("subjects : ", subjects)
print("subjects_2 : ", subjects_2)

subjects.insert(0,subjects_2)                       # It inserts a list and we can also decide where to put it in using the index
print("printing the list with subjects_2 insert in the first index of the subjects : ",subjects)
subjects.remove(subjects_2)                         # It removes the list or elements from the list
print("removed the inserted list again and now printing it again : ", subjects)

subjects.append(subjects_2)                         # It appends or add the list at the end of the list of our choice
print("appended list printing : ",subjects)

subjects.remove("chemistry")                        # Removing the element from the list 
print("printing the list after removing the elements from the list : ",subjects)


poped_element = subjects.pop()     # Pop the last element but we can also use the index to pop the desire elements forn the list
print("Printing the poped element with a variable to store the value of it : ",poped_element)
print("printing the list again after the elements from the last is poped : ",subjects)


subjects.extend(subjects_2)           # Extends the list with another list adds the list together elements wise not as whole list 
print("Printing the extended list here : ",subjects)

num = [12,45,7,89,4]
num.sort()                       #sorts the list in ascending order by default
print("\nprinting the sorted list : ",num)


num.sort(reverse=True)          # sorts the list in the desceding order
print("\n printing the list in descending order : ",num)

