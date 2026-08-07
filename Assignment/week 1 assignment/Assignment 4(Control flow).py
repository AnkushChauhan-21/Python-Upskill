# Task 1 
print("\n---- Task 1 ----\n")
for i in range(3):
    num = int(input("Enter the number here : "))
    if num % 2 == 0:
        print(f"The {num} is a even number ")
    else:
        print(f"The {num} is not even its an odd number here")


# Task 2 
print("\n--- Task 2 ----\n")
string_list = ["civic"  , "oyo" , "hello"]
for str in string_list:
    str_reverse = ""
    for char in str:
        str_reverse = char + str_reverse
    if(str == str_reverse):
        print(f"The {str} is a  palindrome")
    else:
        print(f"The {str} is not a palindrome")


# Task 3 
print("\n--- Task 3 -----\n")
fib = int(input("Enter a number for fibonaci :  "))
if (fib<=0):
    print("Please enter the positive number and bigger than the zero")
else:
    if fib==1:
        value = 0
    elif fib==2:
        value = 1
    else:
        a,b=0,1
        for i in range(3 , fib + 1):
            value = a + b
            a = b
            b = value
        value = b


print(f"The fibonaci {fib} is : ", value)


# Task 4 
print("\n------ Task 4  ------\n")
num = [1,2,3,4,5,6,7]
len = len(num)
pair = [ ]
for i in range(len):
    for j in range(i+1 , len):
        if(num[i]+num[j]==9):
            pair.append(num[i])
            pair.append(num[j])

print("the value pair who is equal to the 9 is : ",pair)


# Task 5 
print("\n---- Task 5 -------")
i = 1
while i<=20:
    if i%2 == 0:
        print("The number is even : ", i)
    i+=1



# Task 6
print("\n------ Task 6 -----")
numbers = [34,345,7,834,234,848,956,23]
searching_num = 23
for num in numbers:
    if(num==searching_num):
        print(f"The {searching_num} has been matched and founded here")
        break

else:
    print(f"The {searching_num} has not been found and the code is terminating now")




# Task 7
print("\n--- Task 7 -----\n")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print (i)
    i+=1


# Task 8
print("\n----- Task 8-----")
for i in range(5):
    if i == 3:
        pass
    print(i)




# Task 9
print("\n-------- Task 9-----------\n")
def type_of_day(day):
    match day.lower():
        case "saturday" | "sunday":
            return "weekend"
        case "monday" | "tuesday" | "wednesday" | "thrusday" | "friday":
            return "weekdays"
        case _:
            return("Invalid day has been input")

print(type_of_day(input("enter the day you wanna know the type of  : ")))
           




        
      

        

                    
        
    

