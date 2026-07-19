# using if elif else to see how it works
temp =int(input("Enter the temperature here : "))
if temp > 45:
    print("The milk to hot  to drink")
elif temp < 40:
    print("The milk is warm enough  to drink")
else:
    print("just drink it as it is")
print("Have a very nice day")


# another example of if elif and else

age =int(input("Enter the age here : "))
if age < 18:
    print("!!!!(invalid age) ")
elif age >= 18:
    print("valid age")
else:
    print("not eligible")
print("Have a very nice day")


# Ternary operator
age = int(input("Enter Your age here: "))
message = "Eligible" if age >= 18 else "not valid age"  # we are writing like we write in simple english using the maths with it 
print(f"You can go ahead as you are {age} old")


#logical operators
print("\n----Logical Operators here---")

experience = input("enter the year of experience here: ")
exp = int(experience)
if exp > 1 and exp < 5:
    print("You can come for interview")
if 3 <= exp <=7:
    print("salary might be not good enough cause we are tight on budget")
if exp < 1 or exp == 0:
    print("You are rejected ")
if not(exp < 1 or exp == 0):
    print("you can try sending your resume")


# short circuting
# short circuting using the and , or ,not which means the evaluation stop as soon as we get a determine result in all these three based on given condition

print("\n--- short circuting---")


high_income = True
credit = True
loan_pending = False
if high_income and credit and not loan_pending:
    print("You can try(eligible) for Loan")
if high_income or credit or loan_pending:
    print("You are can or cannot be eligible for the loan")

else:
    print("Dont try to apply for the loan")
print("Eligiblity is checked and the answer is given do not try again and exit the screen ")