#!/usr/bin/env python3

import csv
import operator
import re

def count_errors():
    error = {}
    per_user = {}

    with open('syslog.log') as file:
        pattern = r"ticky: (INFO|ERROR) (.*) \(([\w\.]*)\)$"
        for line in file:
            results = re.search(pattern, line.strip())
            if results is not None:
                error_type = results.groups()[0]
                error_desc = results.groups()[1]
                username = results.groups()[2]
                if username not in per_user.keys():
                    per_user[username] = {"INFO": 0, "ERROR": 0}
                if error_type == "INFO":
                    per_user[username]["INFO"] = per_user[username]["INFO"] + 1
                else:
                    per_user[username]["ERROR"] = per_user[username]["ERROR"] + 1
                    error[error_desc] = error.get(error_desc, 1) + 1
            else:
                print("No match line:", line)
        print("Errors:", error)
        print("Users:", per_user)
        file.close()
        return error, per_user


def generate_reports(error, per_user):
    sorted_errors = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    sorted_per_user = sorted(per_user.items())
    print("Errors:", sorted_errors)
    print("Users:", sorted_per_user)

    # We have to form a list of dictionaries that includes the column names to pass it to the DictWriter
    keys = ["Error", "Count"]
    rows = []
    for key, value in sorted_errors:
        rows.append( { keys[0]: key, keys[1]: value } )

    with open("error_message.csv", "w", newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=keys)
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        file.close()

    # We have to form a list of dictionaries that includes the column names to pass it to the DictWriter
    keys2 = ["Username", "INFO", "ERROR"]
    rows2 = []
    for key, error_dict in sorted_per_user:
        rows2.append( { keys2[0]: key, keys2[1]: error_dict["INFO"], keys2[2]: error_dict["ERROR"] } )

    with open("user_statistics.csv", "w", newline="") as file2:
        csv_writer = csv.DictWriter(file2, fieldnames=keys2)
        csv_writer.writeheader()
        csv_writer.writerows(rows2)
        file2.close()

if __name__ == "__main__":
    error, per_user = count_errors()
    generate_reports(error, per_user)