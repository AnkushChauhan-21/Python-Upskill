print("---Task 1 ------")
admin_name = input("enter Your name admin : ").upper()
print(f"Welcome Mr/Mrs {admin_name} \n Good Morning , shall we start with todays work")

print("---task 2 ----")
num1 = float(input("enter the desired number for calculation : "))
num2 = float(input("enter the desired number for calculation : "))
sum = num1 + num2
multi = num1 * num2
division = num1 / num2
print(f"so the sum of {num1} and {num2} is {sum}")
print(f"so the multiplication of {num1} and {num2} is {multi}")
print(f"so the division of the {num1} and {num2} is {division}")

print("--task 3 ----")
list_of_names = input("enter the names here please with ',' : ")
names = list_of_names.split(',')
print("Lets print all the names with appropriate gap between them here : ",names)

print("--Task 4---")
Age_verification = int(input("enter the age here to check the eligibilty for yourself (e.g: 18 or any number no flaot) : "))
if Age_verification >= 18:
    print("You are an adult and can do the voting")
else:
    print("You are not eligible for the voting here")


print("--task 5---")
pi = 3.14159
print(f"print only till 2 decimals of pi : {pi:.2f} \n ")


pin = float(input("enter any flaot number with more digits : "))
print(f"print only till 2 decimals of pi : {pin:.2f}")
    