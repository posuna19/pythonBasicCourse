
"""
Capturing groups
Are portions of the pattern that are enclosed in parentheses
"""

import re

text = "Lovelace, Ada"
regex = r"^(\w*), (\w*)$"

result = re.search(regex, text)

print(result)
print(result.groups()) #It returns a tuple with the groups found
print(result[0]) #It contains the whole string matched
print(result[1]) #It contains the first subsequent match in the string
print(result[2]) #It contains the next subsequent match in the string
print("{} {}".format(result[2], result[1])) #Displays the name

# Rearrenge name
def rearrenge_name(name):
    regex = r"^(\w*), (\w*)$"
    result = re.search(regex, name)
    rearrenge_name = name # Default value

    if result is not None:
        lastname = result[1]
        firstname = result[2]
        rearrenge_name = "{} {}".format(firstname, lastname)

    return rearrenge_name

print("Rearrenged Name:",rearrenge_name("Lovelace, Ada"))



"""
In-lesson exercise: Fix the regular expression used in the rearrange_name function so that it can match middle names, 
middle initials, as well as double surnames
"""

def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*.*?)$", name) # Correct regex "^([\w \.-]*), ([\w \.-]*)$"
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")


print(name)