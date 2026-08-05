names = ["logan" , "wade" , "clark" , "bruce" , "tony", "steve"]
heroes = ["wolverine" , "deadpool" , "superman" , "batman" , "ironman" , "captain america"]
print ("zip objects: ", dict(zip(names, heroes)))
# I want ( hero : name) pair for each name and hero in names and heroes


# Lets do this normal way 
my_dict = {}
for name,hero in zip(names,heroes):
    my_dict[name] = hero
print("normal way to do it is ",my_dict,sep = '\n',end = '\n\n')

# using the dictionary comprehension way to do it now
my_dict_comp = {name: hero for name,hero in zip(names,heroes)}
print("its the comprehension way to do it",my_dict_comp,sep = '\n',end = '\n\n')


# if i want to change the name to the upper case we can do it too while doing the dictionary comprehension
my_dict_comp_upper = {name.upper() : hero for name,hero in zip(names,heroes)}
print("its the comprehension way to do it with upper case names",my_dict_comp_upper,sep = '\n',end = '\n\n')


# What if i want to change the name to the upper case and hero to the lower case and also making sure that the length of name is 4 letter lets try that with an example too---


my_custom_dict = {name.upper() : hero.lower() for name,hero in zip(names,heroes) if len(name)<= 4}
print("lets try to print this with so many custom added things in it ",my_custom_dict,sep = '\n',end = '\n\n')


# lets try another one if we want to filter out the one name we dont wanna be print in the dictionary we can do that too at the same time performing all the things we want lets do it with an clear example
my_not_dict = {name.upper() : hero.upper() for name,hero in zip(names,heroes) if name != "wade" }
print("lets try to print this for sure wade will not be printed : ",my_not_dict , sep='\n',end='\n\n')