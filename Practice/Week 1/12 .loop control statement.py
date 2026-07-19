# loop statement = statements that let us alter the execution  flow of loops
# break = break statement cut off the loop or terminate the loop prematurely after a certain condition is met
# continue = it skips the current iteration and jumps to next iteration of the loop
# pass = it act as a placeholder,it does nothing,it is used when a statement is required but not the the action so we use pass so it does not throw an error 


print("\n ---printing the example of the loop statement here")
for i in range(0,10):
    if i == 4:
        print("breaking the loop at i : ",i)
        break
    print("the current iteration of i is : ",i)



print("\n ---printing the example of the continue statement here")
for i in range(0,11):
    if i % 2 == 0:
        print("skipping the even number here : ",i)
        continue
    print("the odd number here : ",i)


print("\n ---printing the example of the pass statement here")
for i in range(1,5):
    if i == 2:
        print(f"we will pass the {i}")
        pass
    print("Apart from pass other values are : ",i)

# pass is used as a place holder for future code which we dont want to do or dont have a need right now so the code will not throw the error here

