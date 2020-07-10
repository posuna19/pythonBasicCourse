file = open("spider.txt")
print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
print()
print("READ method:")
print(file.read())

file.close()

print("Opening a file with the 'with' block, python closes the file automatically: ")
with open("spider.txt") as file:
    print(file.readline())
