# Task 1
import time
print("\n------ Task 1 ------\n")
lists = []


def calculate_the_performance(func):
    def wrapper():
        start_time = time.time()
        print("The start time is executing here : ",start_time)
        func()
        end_time = time.time()
        print("The end time is executing here : ",end_time)
        print("The total time taken in appending the list : {:.6f}seconds".format(end_time - start_time))
    return wrapper



@calculate_the_performance
def func_to_append():
    for i in range(1,1000):
        lists.append(i)

func_to_append()






# Task 2 
print("\n------ Task 2 ------\n")


def retry(num_times):
    def repeat(func):
        def wrapper(*args ,**kwargs):
            for i in range(0,num_times):
                func(*args , **kwargs)
        return wrapper
    return repeat    




@retry(4)
def repeat_this(name):
    print(f"welcome Master {name}!")

repeat_this("Ankush")



# Task 3
print("\n------ Task 3 ------\n")

def validating_the_positive(func):
    def wrapper(*args , **kwargs):
        if(all(arg>0 for arg in args)):
            return func(*args , **kwargs)
        else:
            print("This number is not a positive number,Please enter a positive number here")
    return wrapper

def sqr_root(x):
    return x**0.5

print(int(sqr_root(144)))



# Task 4
print("\n------ Task 4 ------\n")

cache_structure = {}
def cache(func):
    def wrapper (*args , **kwargs):
        value = cache_structure.get(args[0])
        print(f"The value of the cache_structure is {value} for {args[0]}")
        if(value is None):
            print(f"Data for the {args[0]} Not Found!!!!")
            value = func(*args , **kwargs)
            cache_structure[args[0]]=value
        return value
    return wrapper



@cache
def doing_computation(x):
    print("The computation is being done here")
    return x * x


print(doing_computation(5))
print(doing_computation(5))
print(doing_computation(7))
print(doing_computation(7))
        




# Task 5
print("\n------ Task 5 ------\n")

def require_permission(func):
    def wrapper(*args , **kwargs):
        user_name = args[0]['Name']
        user_permission = args[0]['Permission']
        print(f"Checking permissions for {user_name} with permission level {user_permission}")
        if(user_permission.count('Admin')>0):
            func(*args , **kwargs)
        else:
            print("Access Denied")
    return wrapper




@require_permission
def delete_user(user , userId):
    print(f"User {userId} deleted the {user['Name']}")


user1 ={ "Name" : "Ankush" , "Permission" : "Admin"}
user2 ={"Name" : "Ankush" , "Permission" : "Dev"}
user3 ={"Name" : "Ankush" , "Permission" : "user"}


user_list= [user1,user2,user3]
for index , user in enumerate(user_list):
    delete_user(user , index+1)