import csv

file = open("csv_file.csv")
csv_file = csv.reader(file)
for row in csv_file:
    # UNPACK values!
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
file.close()