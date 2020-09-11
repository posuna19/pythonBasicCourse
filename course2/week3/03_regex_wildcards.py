import re

regex = r"[Pp]"
text = "Python, python, ruby, Xython, papa"

result = re.search(regex, text)

print("Result: ", result)

result = re.match(regex, text)
print("Result: ", result)

result = re.findall(regex, text)
print("Result: ", result)

regex = r'[a-z]way'
text = 'The end of the highway'
result = re.search(regex, text)
print("Result: ", result)

text = 'What a way to go'
result = re.search(regex, text)
print("Result: ", result) #It is None because the way word is preceding by a space which is not considered
                          # a letter in the range a-z from the regex


regex = r"cloud[a-zA-Z0-9]"
text = "cloudy"
result = re.search(regex, text)
print("Result: ", result)

text = "cloud9"
result = re.search(regex, text)
print("Result: ", result)


#In-lesson exercise
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#By using the circunflex special char inside the brackets we can set a negation regex
regex = r"[^a-zA-Z]" #This regex matches only non-letter chars
text = "This is a sentence with spaces."
result = re.search(regex, text)
print("Result: ", result) #It matches to the 5th char(index 4) in the string

regex = r"[^a-zA-Z ]" #This matches any char that is not a letter or nor a space
text = "This is a sentence with spaces."
result = re.search(regex, text)
print("Result: ", result) #It matches to last char of the string, which is the period(.)

regex = r"cat|dog"
text = "I like cats"
result = re.search(regex, text)
print("Result: ", result)

text = "I like dogs"
result = re.search(regex, text)
print("Result: ", result)

text = "I like both dogs and cats"
result = re.findall(regex, text)
print("Result: ", result) # Find all functions is used to find several matches, while the search function is used to find
                          # only the first match


regex = r"\d"
text = "I like cats213 dasdasd"
result = re.search(regex, text)
print("Result: ", result)

text = "I like cats213 dasdasd"
result = re.findall(regex, text)
print("Result: ", result)

regex = r"\d+"
text = "I like cats213 dasdasd"
result = re.search(regex, text)
print("Result: ", result)

text = "I like cats213 dasdasd"
result = re.findall(regex, text)
print("Result: ", result)