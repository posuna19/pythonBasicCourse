import re

regex = r"[a-zA-Z]{5}"
text = "a ghost"
result = re.search(regex, text)
print("result 1: ", result)

text = "a scary ghost appeared"
result = re.search(regex, text)
print("result 2: ", result)

result = re.findall(regex, text)
print("result 3: ", result) # It matches the 'appea' word, which is wrong. In order to fix this, we should use the \b

regex = r"\b[a-zA-Z]{5}\b"
result = re.findall(regex, text)
print("result 4: ", result)

# Range of words
regex = r"\w{5,10}"
text = "I really like strawberries but"
result = re.findall(regex, text)
print("result 5: ", result) # It matches the strawberri word limited to 10 chars only

regex = r"\w{5,}" #We can fix the prior issue without indicating the maximun length
result = re.findall(regex, text)
print("result 6: ", result)


# In lesson exercise: The long_words function returns all words that are at least 7 characters. Fill in the regular
# expression to complete this function
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


# In lesson exercise: Add to the regular expression used in the extract_pid function, to return the uppercase message
# in parenthesis, after the process id
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    #print(result.groups())
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)




