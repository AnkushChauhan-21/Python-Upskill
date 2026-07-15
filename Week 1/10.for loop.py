# learning for loops here

print("\n---For loops example below---")

for number in range(4):                                  # iteration from 0 to n-1 range here each one by one
    print("Current number iteration is : ", number)


print("\n")
for string in "BREAK":                                  # iteration of each character one by one
    print("current character from the string iteration : ",string)             


print("\n")  
for x in range(1,5):                                     #iteration from 1 to n-1 as starting is inclusive and ending is exclusive
    print("iteration of range till end one by one : ",x)


print("\n")
for step in range(0,8,2):                             # iteration of range but with steps of two 
    print("printing each iteration with the step of 2 : ",step)


print("\n")
#printing the for loop with the if loop too


successful = False
for attempt in range(1,4):
    print("Attempt No:",attempt)
    if  successful:
        print("Successfully sended to the person")
        break
    elif not successful:
        print("Attempted three times and failed")
        

else:
    print("We will try again later")




#iterables 
# An iterable is an  object that can be iterated over(loop through)
#Lists , tuples , set , strings , dictionaries , range are some examples of iterables


print("\n--iterating through a list---")
apps = ["Facebook" , "instagram" , "whatsapp"]
for app in  apps:
    print("app" , ":" , app)


print("\n--iterating through a string---")
words = "car-is-parked-over-there"
for character in words:
    print("char",":",character)



print("\n--iterating through a dict---")
dict_1 = {"Name" : "Ankush",
          "course" : "Mca" ,
          "Fav_subjects" : ["English" , "Maths"]
          }
for key in dict_1:
    print(key , ":",dict_1[key])



print("\n--iterating through a tuple---")
tup = (10,45)
for x in tup:
    print("x" , ":" , x)
    


print("\n--iterating through a range---")
for i in range(5):
    print(i)


