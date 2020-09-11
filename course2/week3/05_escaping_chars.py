
import re

#*****************************************
# Escaping chars
# What if we want to escape a character?
#*****************************************

regex = r".com" # We want to find a dot in the string... how do we do it?
text = "welcome"
result = re.search(regex, text)
print("Result 1: ", result) # This is NOT the expected result!

regex = r"\.com" # We use the back slash sign to indicate we want to search for the dot in the string
result = re.search(regex, text)
print("Result 2: ", result) # This does not longer match because the welcome word does not have the dot in it

text = "mydomain.com"
result = re.search(regex, text)
print("Result 3: ", result) # This does match!



#*****************************************
# Special Sequences of characters
#*****************************************

regex = r"\w*" # It matches any alphanumeric char: letter, numbers and underscores
text = "This is an example"
result = re.search(regex, text)
print("Result 4: ", result) # This does not match because the space char is not included in the regex

text = "This_is_an1example"
result = re.search(regex, text)
print("Result 5: ", result) #



"""
In lesson Exercise:
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters 
(including letters, numbers, and underscores) separated by one or more whitespace characters.
"""

def check_character_groups(text):
  result = re.search(r"[\w*]+[\s*]+[\w*]+", text)
  #print(result)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False