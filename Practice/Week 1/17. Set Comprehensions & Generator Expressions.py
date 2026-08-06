duplicate = [2 , 4 , 5 ,6,7,6,23,56]

# lets try it noramal way 
my_set = set()
for n in duplicate:
    my_set.add(n)
print("The normal way as we know set dont repeat the same items ",my_set,sep='\n',end='\n\n')


# Lets do it in the comprehension way 
my_set_comp = {n  for n in duplicate }
print("lets try to print in the comprehension way ",my_set_comp,sep='\n',end='\n\n')


# Generators expression
# I want to yield (n*n for each n in nums)

nums = [1,2,3,4,5,6,7,8,9,0]
def gen_func():
    for n in nums:
        yield n*n
gen = gen_func()
print("using the generator function")
for items in gen:
    print(items , end=' ')
print("\n\n\n")

# using the generator expression for the same task
# return_value using expression for items in iterable

gen_exp =(n*n for n in nums)
print(gen_exp)
print("using the generator expression to print the items")
for items in gen_exp:
    print(items,end=' ')
print("\n")
