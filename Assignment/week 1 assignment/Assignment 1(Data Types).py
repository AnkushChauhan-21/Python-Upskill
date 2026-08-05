print("converting one data type to another one \n")
print("\n-------Task 1 --------\n")
float_int = 37.5
string_float = "123"
int_boolean = 0
boolean_string = False

print(f"1.1 Converting the {float_int} to integer {int(float_int)}")
print(f"1.2 Converting the {string_float} to float {float(string_float)}")
print(f"1.3 Converting the {int_boolean} to boolean {bool(int_boolean)}")
print(f"1.4 Converting the {boolean_string}  to string {str(boolean_string)}")


print("\n---- Task 2----")
x = "money"
x_upper = x.upper()
print(f"2.1 The Original string is : {x}")
print(f"2.2 The upper case string is : {x_upper}")

print("\n---- Task 3--------")
x = 2.5
y = 2
z = x + y
print(f"3.1 The type of result of adding {x} and {y} which is {z} : The type of {z} is(Type :: {type(z)})")

print(f"3.2 converting thee type of the result {z} is {int(z)} and type (Type : {type(int(z))}) ")


print("\n--------Task 4 ------------")
s = "Power"
print(f"4.1 Original string is : {s}")
print(f"4.2 upper case of the string is  {s.upper()}")
print(f"4.3 replace : {s.replace('o' , 'l')}")
print(f"4.4 is {s} startwith po or not : {s.startswith('pow')}")
print(f"4.4 is {s} endswith er  or not : {s.endswith('er')}")
