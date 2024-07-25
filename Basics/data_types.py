#1. Text Type:	str
my_text = "Hello World"
print("")
print("String:", my_text)

#2. Numeric Types:	int, float, complex
#Integer
my_int = 10
print("Int:", my_int)

#Float
my_float = 10.5
print(my_float)

#Complex
my_complex = 1 + 2j
print(my_complex)

#3. Sequence Types:	list, tuple, range
#List
emojisList  = ['😀', '😂', '😍', '😎', '😜']
print("List:", emojisList)

#Tuple
emojisTuple  = ('😀', '😂', '😍', '😎', '😜')
print("Tuple:", emojisTuple)

#Range
my_range = range(5)
print("Range:", my_range)   

#4. Mapping Type:	dict
#Dictionary
my_dict = {
    "name": "John",
    "age": 30
}
print("Dictionary:", my_dict)

#5. Set Types:	set, frozenset
#Set
emojisSet = {'😀', '😂', '😍', '😎', '😜'}
print("Set:", emojisSet)

#Frozenset
emojisFrozenSet = frozenset({'😀', '😂', '😍', '😎', '😜'})
print("Frozenset:", emojisFrozenSet)

#6. Boolean Type:	bool
my_boolean = True
print("Boolean:", my_boolean)


#7. Binary Types:	bytes, bytearray, memoryview
#Bytes. Can hold numbers between 0 and 255
my_bytes = [0, 145, 2, 255, 4, 5]
b = bytes(my_bytes)
#b[0] = 255
for byte in b:
    print(byte)

print("---------------")

#Bytearray
my_byteArray = [0, 145, 2, 255, 4, 5]
ba = bytearray(my_byteArray)
ba[0] = 255
for byteArray in ba:
    print(byteArray)


#Memoryview
mv = memoryview(b"Hello")

print(mv)

#return the Unicode of the first character
print("Unicode of the first character:", mv[0])

#return the Unicode of the second character
print("Unicode of the second character:", mv[1])


#8. None Type:	NoneType
my_none = None
print("None:", my_none)



print("")
