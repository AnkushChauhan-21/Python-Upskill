# Generators in Python are a simple and powerful tool for creating iterators.
# They allow you to declare a function that behaves like a iterators,i.e,it can be used in a for loop.
# Generators use the "yield" value to produce a series of values,instead of returning a single value and  terminating


def sqaure_number(nums):
    for num in nums:
        yield num * num

numbers = [1,2,3,4,5,6]
square_values = sqaure_number(numbers)
print(next(square_values))
for sqr in square_values:
    print(sqr , end=' ')
    print("\n")


square_list= list(sqaure_number(numbers))
print(square_list)

# Generators expression
# [return_value using the expression for item in iterable]
gen_exp = (num  * num for num in numbers)
square_exp = list(gen_exp)
print("The values generated using the expression : ",square_exp)