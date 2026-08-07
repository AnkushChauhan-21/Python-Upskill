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
        

                    
        
    

