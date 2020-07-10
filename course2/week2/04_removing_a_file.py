import os

# NOTE: a file has to be created manually first!
# Remove a file
os.remove("fileToRemove.txt")


# Rename a file
os.rename("fileToRename.txt", "fileToRename2.txt")


# Checking if a file exist:
print(os.path.exists("fileToRename.txt"))
print(os.path.exists("fileToRename2.txt"))