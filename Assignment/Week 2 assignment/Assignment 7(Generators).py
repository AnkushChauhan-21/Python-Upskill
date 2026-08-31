# Task 1
print("\n --------- Task 1 ------\n")

def fibonaci_generator():
    a=0
    b=1
    while True:
        yield a
        c = a + b
        a=b
        b=c

gen = fibonaci_generator()
for i in range (1,10):
    print(next(gen))

# Task 2
print("\n ------ Task 2 -----\n")
def multiple_generator(n):
    i=1
    while True:
        yield n*i
        i+=1

multi = multiple_generator(5)
for i in range(10):
    print(next(multi))
    
