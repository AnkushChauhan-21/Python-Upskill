name = input("Enter Your Name Here : ") #inputaa() function always  returns a string
print(f"Hello! , {name} , Welcome to My World")


age = input("Enter Your Age : ")
# Note = we can only concatenate str to str not str to int typeError will show
age_after_one_year = int(age) + 1 #converting the  age to int  so we can perform the arithmetic operations on it 
print(f'Hello This is Your Age after one year : {age_after_one_year} \nHave a good year')


#Lets try taking float as a input now
height = float(input("Enter Your Height here in meters (e.g., 1.57) : "))
#valueError : could not convert str to float
print(f"Hey Wow Your Height is : {height}\nKeep eating healthy and grow much taller")