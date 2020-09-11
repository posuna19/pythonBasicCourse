import re
import sys


usernames = {}
file_name = sys.argv[1]
print("File name {}".format(file_name))
with open(file_name) as file:
    for line in file:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)"
        result = re.search(pattern, line)
        if result is None:
            continue
        user = result[1]
        usernames[user] = usernames.get(user, 0) + 1

print(usernames)