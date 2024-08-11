#1. Creating Variables
a = 5
b = 10
c = a + b
print(c)

#2. Use casting to specify data types
a = str(5) # a will be '5'
b = int(10) # b will be 10
c = float(5) # c will be 5.0

#3. How to get a variable's type
print(type(a))
print(type(b))

#4. Using single and double quotes for strings values
name = 'Amos'
name = "Amos"

#5. Variables are case sensitive
name = 'Amos'
Name = 'Amos'

#6. Naming variables 
animalemojis = '🐶'  
animal_emojis = '🐶' 
_animal_emojis = '🐶'  
animAlemojis = '🐶'  
ANIMALEMOJIS = '🐶' 
animalemojis3 = '🐶' 

#7. Assign values to multiple variables in a single line
r, g, b = 255, 150, 200

#8. Assign the same value to multiple variables in a single line
r, g, b = 255

#9. Extract collection values into variables
fruit_emojis = ['🍒', '🍓', '🍇']
cherry, strawberry, grapes = fruit_emojis

#10. Global and local variables
x = 10
def add():
    global y 
    y = 15
    print(x + 5)
print(x + y)
