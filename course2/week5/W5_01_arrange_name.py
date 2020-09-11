import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name) # Correct regex "^([\w \.-]*), ([\w \.-]*)$"
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

def LetterCompiler(txt):
  result = re.findall(r'([a-c]).', txt)
  if len(result) == 0:
      return txt
  return result

#print("Funtion call:", LetterCompiler("123"))