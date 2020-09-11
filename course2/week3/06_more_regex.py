
import re

#Exercise 1: Find a city name that starts and ends with an a
regex = r"A.*a"
text = "Argentina"
result = re.search(regex, text)
print("Result 1: ", result) # this works

#But what about this other country: Arzerbaijan
text = "Arzerbaijan"
result = re.search(regex, text)
print("Result 2: ", result) # The regex finds a match but it should not because there is a 'n' at the end of the word
                            # so, it should not match anything but it does

#So we have to be more specific and modify our regex as follows
regex = r"^A.*a$"
result = re.search(regex, text)
print("Result 3: ", result) # In this case the regex does not find any match, which is correct!


text = "Australia"
result = re.search(regex, text)
print("Result 4: ", result) # The regex finds a match


#Exercise 2: find a valid variable name in python
regex = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
text = "_this_is_aValid_name"
result = re.search(regex, text)
print("Result 5: ", result)

regex = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
text = "this isn't a valid variable"
result = re.search(regex, text)
print("Result 5: ", result)


# Variable with a number at the end
text = "my_variable1"
result = re.search(regex, text)
print("Result 6: ", result) # It matches!

# Variable with a number at the beginning
text = "2my_variable1"
result = re.search(regex, text)
print("Result 7: ", result) # It does not match because it begins with a number


# IN LESSON Exercise: Fill in the code to check if the text passed looks like a standard sentence, meaning that it
# starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period,
# question mark, or exclamation point.


def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]+[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True