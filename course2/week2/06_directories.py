import os

print("Current directory: " + os.getcwd())
print("Creating a directory: ")
if os.path.exists("subdir"):
    os.rmdir("subdir")

os.mkdir("subdir")
print("Directory subdir was created")
os.chdir("subdir")
print("Directory changed: " + os.getcwd())

print("List of all file in the current directory: ")
os.chdir("..") # go up one level on the current path
print(os.listdir())

# exercise to see all the folder and files from the current directory:
parentDir = "week2"
for item in os.listdir():
    fullname = os.path.join(parentDir, item) # this functions adds a / or \ depending on the OS the script is executed
    if os.path.isdir(item):
        print("{} is a dir".format(fullname))
    else:
        print("{} is a file".format(fullname))


