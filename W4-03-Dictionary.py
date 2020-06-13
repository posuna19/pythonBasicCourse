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


formatNextTopic(" Dictionary {}")

dic = {'jps':12, "txt":23, "csv":56, "pgn":45}
print("Printing type", end=" ")
print(type(dic))
print("Values: " + str(dic))
print("Indexing: " + str(dic['csv']))
print("Using 'in' key word: " + str("pgn" in dic))
dic["doc"] = 84
print("Adding a new value: " + str(dic))
dic["txt"] = 99
print("Replacing a key: " + str(dic))
del dic["doc"]
print("Deleting doc from dic: " + str(dic))
print("With For loop: ")
formatNextTopic("Iteraring over a Dictionary")
for k in dic:
    print(k +" : " + str(dic[k]))
print("With items() method: ")
for key, count in dic.items():
    print("There are {} files with .{} extension".format(count,key))

print("Keys only: " + str(dic.keys()))
print("Values only: " + str(dic.values()))

print("Values only: ")
for v in dic.values() :
    print(v)

formatNextTopic("Counting repeated chars in a text")
def count_letter(text):
	result = {}
	for c in text:
		if c not in result:
			result[c] = 0
		result[c] += 1
	return result

print(count_letter("mm Hi this is a example text, hello xsdawisoo0"))

formatNextTopic("Iteraring dictionary and lists")
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes in wardrobe:
	for color in wardrobe[clothes]:
		print("{} {}".format(color, clothes))

formatNextTopic("Exercise groups and users")

def groups_per_user(group_dictionary):
  user_groups = {}
  # Go through group_dictionary
  for group, users in group_dictionary.items():
	  # Now go through the users in the group
    for user in users:
		  # Now add the group to the the list of
      # groups for this user, creating the entry
      # in the dictionary if necessary
      if user not in user_groups:
        user_groups[user] = [group]
      else:# group not in user_groups[user]:
          user_groups[user].append(group)
  return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)