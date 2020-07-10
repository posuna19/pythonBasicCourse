print("Reading the lines")
with open("spider.txt") as file:
  for line in file:
    print(line)
file.close()

print("**************************")
print("Reading the lines without the end line")

with open("spider.txt") as file2:
  for line in file2:
    print(line.strip())
file2.close()

print("**************************")
print("Getting the lines")
file3 = open("spider.txt")
lines3 = file3.readlines()
file3.close()
lines3.sort()
print(lines3)

print("**************************")
print("Writing to the file")