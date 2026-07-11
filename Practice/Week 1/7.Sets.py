comp_science_courses = {"DSA" , "computer fundamentals" , "operating system" ,"sql" , "advance java"}

print("\n-- printing the original set comp_science_courses ",comp_science_courses)
#the output will not be in order as sets dont care about the order everytime we print the set it will give the different order everytime 


# Adding the element in the set
comp_science_courses.add("python")
print("\n-- printing the set with added element in the set",comp_science_courses)



# removing the element in the set
comp_science_courses.remove("python")
print("\n--printing the set after removing the one element from it : ",comp_science_courses)


# sets are unordered collection with not duplicate elements
dup_set = {"23" , "money"  , "unauthorized","banana","unauthorized"}
print("\n printing the set with duplicate elements here : ",dup_set)


courses = {"DSA","operating system","sql","Hindi","english"}
print("\n---printing this set too : ",courses)



# Set operations

print("\n---Sets operations here--")
print("\nunion of two sets comp_ or courses : ",comp_science_courses.union(courses)) #union of the two sets here (combines the both sets together)

print("\n now intersection between the two sets (comp_ and courses) : ", comp_science_courses.intersection(courses))
"""
this will show the intersection of the two sets which are mentioned above intersection  is basically the common elements that are present in the both of the sets so the printed set will has the common elements of the both sets and nothing else
"""

print("\ndifference ( comp_ - courses) : ", comp_science_courses.difference(courses)) # it means show the elements present in the comp_ but not the elements of the courses set 

print("\n difference (courses - comp_) : ",courses.difference(comp_science_courses)) # in this we want the elements of the courses but not the elements present in the comp_ set 

print("\nsymmetric difference--- : ",comp_science_courses.symmetric_difference(courses))
# symmetric difference means the all the elements will be printed in both sets but not the intersection elements means the common elements in both the sets will not be printed 







