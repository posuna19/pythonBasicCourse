

try:
    file = open("somefile")

except OSError: # This code is executed ONLY if the 'try block' code raises an OSError
    file = None

print("File: ", "File error" if file is None else "Success")