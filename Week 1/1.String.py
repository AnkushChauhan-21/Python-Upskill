# Printing the welcome message 
message = 'Hello World' 
#Make variable name as descriptive as possible

#we can use the escape character to print the single quote in our string
message_with_quote = 'It\'s a beautiful day!'

#we can also use double quotes to avoid using the escape character to add the single quote
message_with_double_quotes = "It's a beautiful day!"

#we can also use triple quotes to add multiple lines in our string
message_with_triple_quotes = """Using triple quote we can add multiple lines 
like this in our string and
 the triple quotes can be either 
 single 
 or double quotes"""

#printing all the variables
print(message)
print(message_with_quote)
print(message_with_double_quotes)
print(message_with_triple_quotes)


print('\n---String Operations---')
# String operations to check the length and type of the string
print("Length of the message variable is:",len(message))
print("Type of the message variable is:",type(message))



print("\n---String Indexing and Slicing---")
# using index to access the characters in the string
print(message[0]) #prints the first character of the string as indexing starts from 0
print(message[-1]) # prints the last character of the string as negative indexing starts from -1
print(message[4]) # prints the character on the 4 index from the starting
print(message[-5]) #prints the -5th index character from the last



print("\n---String Slicing---")
# using slicing tp access  a range of character in the string
print(message[0:5]) #prints the characters from index 0 to 4 as starting index is inclusive and the ending index is exclusive
print(message[:11]) #prints the characters from start as if we dont provide the starting index it will take it as 0 and prints till the ending index as 11
print(message[0:]) #prints the characters from index 0 to 10 as starting index is inclusive and the ending index is exclusive and we can also leave the ending index blank to print till the end of the string same as starting
print(message[6:10])#prints from 6 index to 9 index 

print(message[-11:-1]) #prints from -11 index to -1 as the ending is exclusive 


print("\n---string slicing with step---")
print(message[0:11:2]) #prints the characters from index 0 to 10 with a step of 2
print(message[0:11:3]) #prints the characters from index 0 to 10 with a step of 3
print(message[-1:-12:-1]) #prints the charcters from -1 index to -11 with a step of -1 which means it will print the character in the reverse order
print(message[-1:-12:-3]) #prints the charcters from -1 index to -11 with a step of -3 which means it will print the character in the reverse order


print("\n---String Methods---")
print(message.upper()) #prints the string in upper case
print(message.lower()) #prints the string in lower case
print(message.count('o')) #prints the count of the character 'o' in the string
print(message.find('o')) #prints the index of the first occurrence of the character 'o' in the string
message_new = message.replace('World','Python') #replaces the word 'world' with 'Python' in the string
print(message_new) #prints the new string after replacing the word 'world' with 'Python'
print(message.split(' ')) #splits the string into a list of words based on the space character
print(message.startswith("Hello")) #checks if the string starts with the word with "Hello" and returns True or False
print(message.endswith("World")) #checks if the string ends with the word "World" and returns True or False
print(message.capitalize()) #capitalizes the first character of the string
print(message.title()) #Title case the string which means it will capitalize the first character of each word in the string
print(message.strip()) #removes the leading and trailing whitespaces from the string
check = "alphabets"
print(check.isalpha()) #checks if all the characters in the string are alphabets and returns True or False
print(message.isdigit()) #checks if all the characters in the string are digits and returns True or False
print(message.isalnum()) #checks if all the characters in the string are alphanumeric and returns True or False
print(message.index('o')) #prints the index of the first occurrence of the character 'o' in the string and raises an error if the character is not found


print("\n---Immutability in Strings---")
#Strings are immutable which means we cannot change the charactera in the string once it is created.We can only create a new string with the chanages we want
orignal_string = "hello python" #the original string is created
modified_string = orignal_string.replace('python','world') 
print("Original String:",orignal_string) #prints the original string and the string is unchanged 
print("modified_string" , modified_string) #prints the new string with the changes we made


print("\n---String Concatenation and repetition ---")
#String Concatentation
greetings = "Hello"
name = "ankush"
message = greetings + " , "  + "Master " + name + " Welcome!"
message2 = '{} , master {} Welcome!'.format(greetings,name)
message3 = f'{greetings} , master {name} Welcome!' 

#we can only concatenate strings with strings and not with other data types like int,float etc.
print(message)
print(message2)
print(message3)

#repetition
repeat_this = "power " * 3 # repeats the string 3 times
print(repeat_this) #prints the string 3 times

print(dir(str)) #prints all the methods available for the string class
#print(help(str)) #prints the documentation for the string class and its methods like what they actually do and how to use them
#print(help(str.upper)) #prints the documentation for the upper method of the string class and how to use it 