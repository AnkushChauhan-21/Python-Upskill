# exception handling
# Different types of block : try , except, else, finally, raise

print("exception handling and error")

# Lets try the basic try-excpetion with an example
try:
    num =int(input("Enter the number : "))
    div = 10/num
    print(f" The result is {div}")
except ZeroDivisionError:
    print("Error! : The value cannot be divided by the zero")
except ValueError:
    print("Error! Invalid input Please Input the integer")


# Example Using the else and finally
print("\n")
try:
    file = open("sample.text" , "r")
except FileNotFoundError:
    print("The file name may be incorrect plzz check it again")
else:
    content = file.read()
    print(content)
    print(" file content  read  successfully")
finally:
    print("The try and except is executed perfectly")

def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    print(f"Your age is {age}")
try:
    user_age = int(input("Enter you age here : "))
    check_age(user_age)

except ValueError as ve:
    print(f"Error! {ve}")
