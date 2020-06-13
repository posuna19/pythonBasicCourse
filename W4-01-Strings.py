
def formatNextTopic(title):
    formatedTitle = "***** " + title + " ****"
    totalLength = len(formatedTitle)
    separator = ""

    for x in range(totalLength):
        separator += '*'

    print()
    print(separator)
    print(formatedTitle)
    print(separator)


#String multiplication
formatNextTopic('String multiplication')
print("Fabiola " * 4)
print(type("asd"))
#String slice or substring
formatNextTopic('String slice or substring')
name = 'Pedro'
print('Name: Pedro, substring[2:4]=', name[2:4])


#Indexing a String
formatNextTopic('Indexing a String')
word = 'The corona virus is spreading'
print('word: ' + word)
print("any chars after index 4 of 'word[4:]' = " + word[4:] ) # from index 4 to len-1
print("first 4 chars of 'word[:4]' = " + word[:4] ) # from index 0 to 3


"""
-- Lecture --
String indexing allows you to access individual characters in a string. You can do this by using square brackets 
and the location, or index, of the character you want to access. It's important to remember that Python starts 
indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an 
index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying 
to access something that doesn't exist! You can also access indexes from the end of the string going towards 
the start of the string by using negative values. The index [-1] would access the last character of the string, 
and the index [-2] would access the second-to-last character.

You can also access a portion of a string, called a slice or a substring. This allows you to access multiple 
characters of a string. You can do this by creating a range, using a colon as a separator between the start 
and end of the range, like [2:5]. This range is similar to the range() function we saw previously. It includes 
the first number, but goes to one less than the last number. You can also easily reference the start or end of 
the string by leaving one value blank. For example [:5] would give us all characters from the start to the 
fourth character in the string. We can also use [5:] to get the characters from the fourth character to the 
end of the string.
"""

formatNextTopic('String.index method')
w2 = "Cats & dogs"
print('w2.idex("&") = ' + str(w2.index('&')))
# print('w2.idex("x") = ' + str(w2.index('x'))) # It throws a ValueError, substring not found
# we can avoid the Value Error using in as the following code
if "x" in w2 :
    print('w2.idex("x") = ' + str(w2.index('x')))
else:
    print("Substring 'x' not found in w2 variable")

formatNextTopic('String and in reserved word')
w2 = " Cats & Dogs "
print('Cat is in w2 = ' + str("Cat" in w2))


formatNextTopic("String methods: upper, lower and strip")
print("'" + w2 + "' -> w2.strip() -> '" + w2.strip() + "'")
print("'" + w2 + "' -> w2.lstrip() -> '" + w2.lstrip() + "'") # Removes the blank spaces from the left only
print("'" + w2 + "' -> w2.rstrip() -> '" + w2.rstrip() + "'") # Removes the blank spaces from the right only
print("'" + w2 + "' -> w2.lowe() -> '" + w2.lower() + "'")
print("'" + w2 + "' -> w2.upper() -> '" + w2.upper() + "'")

strNumber = '12345'
formatNextTopic("String other methods: count, endsWith,  isnumeric")
print("'" + w2 + "' -> w2.count('s') -> " + str(w2.count('s')))
print("'" + w2 + "' -> w2.endsWith('Dogs ') -> " + str(w2.endswith('Dogs ')))
print("'" + w2 + "' -> w2.isnumeric() -> " + str(w2.isnumeric()))
print("'" + strNumber + "' -> strNumber.isnumeric() -> " + str(strNumber.isnumeric()))

formatNextTopic("String converting to int")
num = int(strNumber)
print('String value: ' + strNumber + ' -> int value: ' + str(num) + " checked with type function: " + str(type(num)))

formatNextTopic("String joing method")
print(" ".join(['this', 'is', 'a', 'string']))
print('...'.join(['this', 'is', 'a', 'string']))

formatNextTopic("String split method")
str = "This, is, a phrase, separated by, comma" # it returns a list of words separated by a comma without the commas
print(str.split(','))
str = "This is a phrase separated by spaces"
print(str.split())

formatNextTopic("String and format method")
w3 = "Mary"
w4 = 29
print("Hi {}, your age is {}".format(w3, w4))
print("Hi {name}, your age is {age}".format(name=w3, age=w4))

price = 7.5
withTaxes = price * 1.09
print(price, withTaxes)
print("The base price i s ${:>8.2f} and with taxes is ${:>6.2f}.".format(price, withTaxes))