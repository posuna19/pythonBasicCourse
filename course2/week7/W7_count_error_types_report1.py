import re
import csv

def count_error_types(dict, pattern, line):
    results = re.search(pattern, line.strip())
    if results is not None:
        error_type = results.groups()[0]
        dict[error_type] = dict.get(error_type, 1) + 1

def count_error_by_username(dict, pattern, line):
    results = re.search(pattern, line.strip())
    if results is not None:
        error_type = results.groups()[0]
        username = results.groups()[1]

        if username not in dict.keys():
            dict[username] = { "INFO" : 0 , "ERROR" : 0}

        if error_type == "INFO":
            dict[username]["INFO"] = dict[username]["INFO"] + 1
        else:
            dict[username]["ERROR"] = dict[username]["ERROR"] + 1

# Dictionary to count the error types
errorTypes = {}

# Dictionary to count the errors by user
errorByUser = {}

with open('syslog.txt') as file:
    error_type_pattern = r"ticky: (\w*):"
    error_by_user_pattern = r"ticky: (INFO|ERROR):.*\((\w*)\)$"
    for line in file:
        count_error_types(errorTypes, error_type_pattern, line)
        count_error_by_username(errorByUser, error_by_user_pattern, line)
    file.close()

# Report 1
# By using a lambda the Dictionary is sorted by its value instead of the key
sortedErrors = sorted(errorTypes.items(), key=lambda x: x[1], reverse=True)

# We have to form a list of dictionaries that includes the column names to pass it to the DictWriter
keys = ["Error_type", "Occurrences"]
rows = []
for k,v in sortedErrors:
    rows.append({ keys[0] : k , keys[1] : v })

with open("Report1_error_types.csv", "w", newline="") as file2:
    csv_writer = csv.DictWriter(file2, fieldnames=keys)
    csv_writer.writeheader()
    csv_writer.writerows(rows)
    file2.close()

# Report 2
sorted_errors_by_users = sorted(errorByUser.items())

keys2 = ["Username", "INFO", "ERROR"]
rows2 = []
for key,error_dict in sorted_errors_by_users:
    rows2.append({ keys2[0] : key , keys2[1]: error_dict["INFO"], keys2[2]: error_dict["ERROR"] })

# Write the dic to a file. What Format
with open("Report2_error_by_user.csv", "w", newline="") as file2:
    csv_writer = csv.DictWriter(file2, fieldnames=keys2)
    csv_writer.writeheader()
    csv_writer.writerows(rows2)
    file2.close()
