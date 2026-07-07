# Understanding the basics of Input and Output
print("\n---Understsanding the basics of Input and Output---")
number = input("Enter the Number here (e.g.,2,3...) : ")
print("The type of number : ", type(number))
#the type will be string because input() returns a string value unless we add int or float before it 


#By Default the output that  print() produces separates the  objects by  single space and appends the new line to the end of the  output
first_name = "Ankush"
last_name = "Chauhan"
print("Name : ",first_name,last_name)


#Printing  Arrays
print("\n---Printing Arrays----")
arrays = [1,2,3,4,5,6,5]
print(f'The arrays is : {arrays}')
print('arrays',arrays)


age = 45
print("The age is : ", age)

#Printing Dictionaries
print("\n---Printing Dictionaries--")
full_name = {
    "first name" : "Ankush",
    "last name"  : "Chauhan"
}

print("Your Full name is : ",full_name)


#printing the len() function
print("Printing the len() function",len)



#separate and end parameters
print("\n---separate and end parameters---")
print("This","how","we",'seprate', sep="+") #custom separator
print(" I am gonna end this line with ",end="((()))\n")
print("That was fun ending")



#flush and file parameters of print() Function
import sys

print("this is printed to standard output",file=sys.stdout)
print("this is printed to standard error",file=sys.stderr)
print("this is printed immediately",flush=True)





