# i want 'n' values for each 'n' value in nums list
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = []


print("'n' values for each 'n' in nums list")
for n in nums:
    my_list.append(n)
print("Normal way to print it is ", my_list)


# Lets try the list comprehension way to do it now 

my_list_with_comp = [n for n in nums]
print("comprehension way to do it ", my_list_with_comp)

# Comprehension way is much readable and easy to understand than the normal way of doing it.

# now i want 'n*n' values for each 'n' in nums list
print("\n 'n*n' values for each 'n' in nums list")
my_list_sqr = []
for n in nums:
    my_list_sqr.append(n*n)
print("normay way to do it is ",my_list_sqr)

# Lets try the list comprehension way to do it now
my_list_sqr_with_comp = [n*n for n in nums]
print("its the comprehension way to do it",my_list_sqr_with_comp)

# Using the map and lamba for this same task 
my_list_sqr_map = list(map(lambda n:n*n,nums))  # map(function,iterable), converts each item using the function

print("its the map and lambda way to do it",my_list_sqr_map)



# now i want 'n' values for each 'n' in nums list if "n" is even

print("\n 'n' values for each 'n' in nums list if 'n' is even")
my_list_even = []
for n in nums:
    if n%2 == 0:
        my_list_even.append(n)
print("normal way to do it is ",my_list_even)


# lets use the list comprehension way to do it now
my_even_list_comp = [n for n in nums if n%2 == 0]
print("its the comprehension way to do it",my_even_list_comp)


# Lets use the filter and lambda way to do it now
my_filter_even_list = list(filter(lambda n:n%2 == 0,nums))
print("its the filter and lambda way to do it",my_filter_even_list)


# I want (letter,num) pair for each letter in 'abcd' for each num in '1234'
my_list_pair = []

for letter in 'abcd':
    for num in range(5):
        my_list_pair.append((letter,num))
print("its the normal way to do it",my_list_pair)



# lets use the list comprehension way to do it now
my_pair_comp = [(letter,num) for letter in 'abcd' for num in range(5)]
print("its the comprehension way to do it",my_pair_comp,sep = '\n')

# IMPORTANT NOTE ---
# The value/variable name written in the left must match the ones in the loops
# The order of the loops must be same as the written in the left
#The parenthesis arounf the (letter,num) are necessary to create the tuple
# You can use the other data structures like list(letter,num) or dict(letter:num) or set(letter,num) instead of tuple (letter,num) as per your requirement
