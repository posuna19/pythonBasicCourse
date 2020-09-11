import re

regex = r"Py.*n"
text = "Pygmalion"
result = re.search(regex, text)
#It search for the letters Py and n. The .* means any length of characters and it will find as many as possible
print("Result: ", result)

text = "Python Programming"
result = re.search(regex, text)
#In this case, the match spans the whole string
print("Result: ", result)

regex = r"Py[a-z]*n" #Matches any letter only
result = re.search(regex, text)
print("Result: ", result)

regex = r"Py[a-z]*n" #Matches any letter only
text = "Pyn"
result = re.search(regex, text)
print("Result: ", result)

#Repetetive qualifiers: + and ? signs
regex = r"o+l+" #It matches at least 1 'o' letter and 1 'l' letter
text = "golfish"
result = re.search(regex, text)
print("Result: ", result)

text = "woolly"
result = re.search(regex, text)
print("Result: ", result)

text = "boil" #this text it has an 'i' between the two letters, hence, the pattern does not match
result = re.search(regex, text)
print("Result: ", result)


#In-lesson exercise
"""
The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) 
at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. 
"""
import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


regex = r"p?each" #It matches at zero or 1 'p' letter
text = "To each their own"
result = re.search(regex, text)
print("Result: ", result)

text = "I like peaches"
result = re.search(regex, text)
print("Result: ", result)


