import re

# Using split function with regex
regex = r"[!?.]"
text = "One sentence. Another one? And the last one!"
result = re.split(regex, text)
print("result 1: ", result) # The notation marks are NOT included!

regex = r"([!?.])"
result = re.split(regex, text)
print("result 2: ", result) # The notation marks ARE now included!



# Using the Sub function to replace a text with regex
regex = r"[\w.%+-]+@[\w.-]+"
text = "Received an email for go_nuts95@my.example.com"
result = re.sub(regex, "[REDACTED]", text)
print("result 3: ", result) #The email was replaced, hiding the email from the sentence


# Using capturing groups indexes to rearrange the name
regex = r"^([\w .-]*), ([\w .-]*)$"
text = "Lovelace, Ada"
result = re.sub(regex, r"\2 \1", text) # The second parameter uses backtracking,
                                       # the number 2 represents the group at the index 2 from the group list
print("result 4: ", result)


# In lesson excercise: We want to split a piece of text by either the word "a" or "the", as implemented in the
# following code. What is the resulting split list?
result = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(result) # Expected result: ['One sentence. Ano', 'r one? And ', ' l', 'st one!']


