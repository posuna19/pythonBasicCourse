#!/usr/bin/env python3

import subprocess

print(subprocess.run(["date"], shell=True)) #In windows does not work, in linux it

print("hi")

subprocess.run(["sleep", "3"], shell=True) #It works in linux, in windows it does not (more config is needed)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True, shell=True)
print("Result code: ", result.returncode)
print("STD Output: ", result.stdout) # The output returned is in bytes, The 'b' at the begining of the string tell us
# that the string was treated as a set of bytes and python does not know what encoding to use to represent it.
# So we can use the decode function to transform an array of bytes into a UTF-8 (default) String as follows
print("Decoded Output: ", result.stdout.decode().split())


# Checking the Standard Error Stream
# Let's run the rm command to remove a file that does not exist
command = ["rm", "file_does_not_exist.txt"]
result = subprocess.run(command, capture_output=True, shell=True)
print("Return code:", result.returncode)
print("STD output:", result.stdout)
print("STD error:", result.stderr.decode().split())






