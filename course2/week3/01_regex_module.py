import re
log = "July 31 07:51:48 mycoputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print("Results: ", result[1])


regex = ".cat"
result = re.search(regex, "linuxFile.txt")
print(result)