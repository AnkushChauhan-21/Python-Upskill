# while loop = its a kind of loop that allows the code to execute repeatedly based on the given boolean condition
# lets take an example of while loop

Temperature = int(input("Enter the room temperature here: "))
while Temperature < 0 or Temperature > 30:
    print("invalid temperature ")

print(f"You entered {Temperature} As a temperature")