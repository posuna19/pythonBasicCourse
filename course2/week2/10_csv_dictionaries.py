import csv

print("Reading from a dictionary: ")
with open("user_list.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("{} has {} users ".format(row["name"], row["users"]))
file.close()

print("\nWriting using a dictionary: ")

users = [ {"name": "Sol Mansi", "username": "solm"},
	{"name": "Lio Nelson", "username": "lion"},
	{"name": "Charlie Grey", "username": "grey"}]

keys = ["name", "username"]

with open("by_deparment.csv", "w", newline="") as by_deparment:
	writer = csv.DictWriter(by_deparment, fieldnames=keys)
	writer.writeheader()
	writer.writerows(users)
by_deparment.close()

with open("by_deparment.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Name: {}, Username: {} ".format(row["name"], row["username"]))