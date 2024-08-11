# Description: This is a simple Python program that prints a greeting to the user.
# def main():
#     print("Hello, Amos!")
#     name = input("What is your name? ")
#     print("Nice to meet you, " + name + "!")

# This is the standard boilerplate that calls the main() function.
# if __name__ == "__main__":
#     main()

# Data types
# 1. int
myint = 7
print("Integer:", myint)

# 2. float
myfloat = 7.0
print("Float:", myfloat)
# Arithmetic operations
print(myfloat + 0.1)
print(myfloat % 0.1)
print(myfloat ** 0.1)

# User input
name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

# Find sum of two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = float(num1) + float(num2)
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

# All comparison operators
print(myfloat == 8.0)
print(myfloat != 8.0)
print(myfloat > 8.0)
print(myfloat < 8.0)
print(myfloat >= 8.0)
print(myfloat <= 8.0)

# All logical operators
print(myfloat == 7.0 and myfloat == 8.0)
print(myfloat == 7.0 or myfloat == 8.0)
print(not myfloat == 7.0)

# Basic data types
# 3. string
mystring = "Hello"
print("String:", mystring)
print("1st e occurrence is", mystring.find("e")) # Find the index of the first occurrence of the letter 'e'
print(mystring.replace("e", "a")) # Replace all instances of the letter 'l' with the letter 'r'
print('o' in mystring) # Check if the letter 'o' is in the string

# 4. myboolean = False
myboolean = False
print("Boolean:", myboolean)

# Compound data types
# 5. list
mylist = [1, 2, 3]
print("List:", mylist) # Default representation of a list
print("List:", mylist[0])
# Negative index
# -1 refers to the last element, -2 refers to the second last element, and so on
print("List:", mylist[-1])
print("List:", mylist[0:2]) # Get the first two elements. The first index is inclusive and the second index is exclusive

# List methods
mylist.append(4) # Add an element to the end of the list
print("Append 4:", mylist)
mylist.insert(1, 5) # Insert the number 5 at index 1
print("Insert 5 at index 1:", mylist)
mylist.remove(3) # Remove the number 3 from the list
print("Remove 3 from the list:", mylist)
mylist.pop(1) # Remove the element at index 1
print("List:", mylist)
mylist.reverse() # Reverse the order of the list
print("List:", mylist)
mylist.sort() # Sort the list in ascending order
print("List:", mylist)
# print(mylist.clear) ## Remove all elements from the list


# 7. tuple. Tuples are immutable, meaning that you cannot change the elements of a tuple once it is assigned.
mytuple = (1, 2, 3)
print("Tuple:", mytuple)

# 7. dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", mydict)

# Accessing list and tuple elements
print("my list index 0:", mylist[0])
print("my tuple index 1:", mytuple[1])

# Slicing list and tuple
print("Get all elements", mylist[0:3]) ## Get all elements

# Use a step value to get every second element
print("Skip index the second index", mylist[0:3:2])

# Use a negative step value to get every second element in reverse order
print("Get all elements in reverse order", mylist[::-1])

# Get dictionary value
print("Get dictionary value", mydict['a'])

# Type conversion
# built-in functions to convert between types
# floar(), int(), str(), bool()

print("Convert integer to float", float(myint))
print("Convert integer to string" + str(myint))

# Local and global variables
def myfunc():
    global mystring
    mystring = "World"
    print("Local variable:", mystring)
print("Global variable:", mystring)

# Delete a variable
del myint ## Delete integer variable

# If statement
temperature = 20
if temperature > 30:
    print("It's warm")
elif temperature > 20: # else if
    print("It's nice")
else: print("It's cold in Helsinki")

# While loop
count = 0
while count < 5:
    print(count)
    # Increment the count else it will run forever. This is called an infinite loop
    count += 1

i = 1
while i < 6:
    print(i * '*')
    i += 1

# For loop puts the list items on new lines
emojis = ['😀', '😂', '😍', '😎', '😜']
for emoji in emojis:
    print(emoji)

# Functions
def myfunc():
    # Function body
    print("Hello from myfunc!")
# All the following are the same
myfunc()
print(myfunc())

# Range function: Generate a sequence of numbers
myrange = range(5)
# myrange = range(1, 5)
# myrange = range(1, 5, 2) # Start, stop, step
for i in myrange:
    print(i)

# Conditional structures

# Loops

# Classes

