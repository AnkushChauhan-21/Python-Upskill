# Task 1 
print("\n------ Task 1 ------------")
def area_of(lenght,width=10):
    return lenght * width

area_1 = area_of(20)
area_2 = area_of(20,3)
print(f"Lets print the first area first then we can go to the next area :{area_1} ") 
print(f"Lets print the area of the area_2 here and see the answer as we also gave it a width : {area_2}")

# Task 2
print("\n----- Task 2 ----------")
def factorial(n):
    if (n<0):
        return("That invalid as negative numbers dont have the factorials")
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)

print(factorial(int(input("Enter the number for factorial : "))))


# Task 3 
print("\n-------- Task 3 ---------")
def reverse_str(str):
    new_string = " "
    for char in str:
        new_string = char + new_string
    return new_string

print(reverse_str(input("Enter the string you wanna reverse it : ")))

# Task 4
print("\n----- Task 4 -----")
def merge_sum(list1,list2):
    add = None
    add = individual_sum(list1)
    add+= individual_sum(list2)
    return add

def individual_sum(list):
    sum = 0
    for n in list:
        sum+=n
    return sum 

a =[1,2,3,4,5,] 
b =[1,2,3,4,5,] 

print(merge_sum(a,b))


# Task 5
print("\n------ Task 5 ------")
a = [1,2,4,6,6,83,5,257,8,35,14]
def sort_it_out(element):
    element.sort()
    sorted_list= [ ]
    unique_elements = set()
    for ele in element:
        if(ele  not in unique_elements):
            unique_elements.add(ele)
            sorted_list.append(ele)
    return sorted_list


print(sort_it_out(a))