student_info = {
    "Name" : "Ankush Chauhan",
    "age" : "20",
    "courses" : ["BCA" , "MCA"]
}

print("\n-- printing the dictionaries here : ", student_info)

# Accessign the values of the dictionaries
print("\n asking for the value of the key : ",student_info["Name"]) 
print("\n using get to get the same value of the \"Name\" : ",student_info.get("Name"))
print("\n age value : ",  student_info["age"])
print("\n courses value : ",  student_info["courses"])

# Quick note if we use simple value access and the written key is not present in the dictionary it will raise an error but when we use the get() function and the key is not present it will give "none" in the return as a value and will not raise an error 


# Accessing the value of the key using the get() 
print("\n value of the name : ", student_info.get("Name"))
print("\n value of the key that not exist here : ",student_info.get("animals"))
print("\n printing the value of the non existent key but also givng it a value to show : ", student_info.get("Money","This is wrong it does not exist"))


# Adding and updating the key- value pair in the dictionary
student_info["age"] = 25  # updated the age 
student_info["Marks"] = 450  # added a new key-value pair in the dictionary
print("\n printing the updated/added dictionary : ",student_info , sep="\n")


# using the update() to add/upadate multiple key-value pairs
student_info.update({"Revenue" : "23 million" , "investment" : "12 million" })
print("\n printing the updated dictionary here : ", student_info)


# Removing the key-value pairs
age = student_info.pop("age")   # removes the key and return its value
print("\n printing the pop item : ",age)

del student_info["Marks"] # removes the key-value pair 
print("\n printing the dictionary after del : ",student_info , sep="\n")


# using the pop() to remove the last inserted key-value pair
last_k = student_info.popitem()
print("\n printing the pop item here ; ",last_k)
print("\n printing the dictionary after the pop item here : ",  student_info)

# Dictionary methods

print("\n printing all the keys here : ",student_info.keys())
print("\n printing all the values here : ", student_info.values())
print("\n printing all the key-value pair here : ", student_info.items())
print("\n printing the length of the dictionary here : ",len(student_info))



# using the loop in the dictionary here 
print("\n looping through the keys : ")
for key in student_info:
    print("key" , ":" , student_info[key])




print("\n looping through the items")
for key , value in student_info.items():
    print(key , "="  , value)



# nested dictionaries
student = {
    "student1" : {"name" : "ankush" , "marks" : "450/500"} ,
    "student2" : {"branch" : "computer" , "fav_subject" : "computer"}
}

print("\n printing the student here  : ",student)
print("\n accesing the nested key : ", student["student1"]["name"])
print("\n accesing the nested key : ", student["student2"]["branch"])


# lets create the empty dictionary 
empty_dic = dict()
print(type(empty_dic))


# or we can also do this 

dictt = {}
print(type(dictt))


