import re

exp = r"aza"
text = "plaza,12aza,axa,23saza"
result = re.search(exp, text )
print('Search 1: ', result)


exp = r"aza"
text = "pileazarr"
result = re.search(exp, text )
print('Search 2: ', result)


exp = r"aza"
text = "mile"
result = re.search(exp, text )
print('Search 3: ', result)


print('Search 4: ', re.search(r"^x", "xenon"))
print('Search 5: ',re.search(r"p.ng", "penguin"))

print('Search 6: ',re.search(r"p.ng", "Pangaea", re.IGNORECASE))

#Exercise question
def check_aei (text1):
  result = re.search(r"a.e.i", text1)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


