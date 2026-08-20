# Task 1

print("\n----- Task 1 ------\n")
numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7]
print("The Orignal List is : ",numbers)

# Task 2
print("\n----- Task 2 ------\n") 
all_positive = all(num > 0 for num in numbers)
print("All Numbers are positive : ",all_positive)


# Task 3
print("\n----- Task 3 ------\n") 
At_least_even = any(num % 2==0 for num in numbers)
print("At least one number is even : ",At_least_even)


# Task 4
print("\n----- Task 4 ------\n")
divisible = [ 1,2,5,10,60,45,60]
print("The Orignal List is : ",divisible)
div_5 = any(num % 5==0 for num in divisible)
print("If any num is divisible by 5 : ",div_5)
