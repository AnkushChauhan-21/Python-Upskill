num = 45
num_float = 45.6

print(type(num))
print(type(num_float))


#Arithmetic operations on integers and floats
print("\n---Arithmetic Operations---")

a = 34
b = 3
c = 2
d =3

print("Addition : ",a+b)    #Addition
print("Subtraction : " ,a - b)  #Subtraction
print("Multiplication : " ,a*b)  #Multiplication
print("Division : ", a/b)   #Division(float Result)
print("Floor Division : " ,)  #Division(integer Result)
print("Modulus :  ",a%b)  #Modulus (give remainder of the Division)
print("Exponent : ", c**d)  #Exponent (gives the power of the number)


#Short hand operators
print("\n---Short hand operators---")
x = 6 
print("original value of x is : ", x)

x += 1  #x = x +1
print("After x +=1 the value of x is : ",x)

x -= 2 # x = x -1 
print("After x =-1 the value of x is :", x)

x *= 3 #x = x * 3
print("After x *=3 the value of x is :",x)

x /= 3 #x =x / 3
print("After x /=3 the value of x is : ", x)

x **= 2 #x = x **2
print("After x **=2 the value of x is : ", x)


#Comparison operators
print("\n---Comparison Operators---")

p = 23
q = 10

print("p == q : ", p == q ) #Equal to
print("p != q : ", p != q ) # not Equal to
print("p > q : ", p > q ) #greater than
print("p < q : ", p < q ) #Less than
print("p >= q : ", p >= q ) #greater than or equal to 
print("p <= q : ", p <= q ) # Less than or equal to


#Type conversion
print("\n---Type Conversion---")

int_digit = 10
float_digit = 4.4
string_digit = "7"

print("Integer to Float : ",float(int_digit)) #Integer to Float
print("Float to Integer : ",int(float_digit)) #float to Intger
print("String to Integer : ",int(string_digit))  #String to Integer
print("String to float : ",float(string_digit))  #String to float
print("Integer to string : ",str(int_digit))  #Integer to string
print("Float to string : ",str(float_digit)) # Float to string


#warning / Note = Converting the non-numeric strings to numbers will raise an error