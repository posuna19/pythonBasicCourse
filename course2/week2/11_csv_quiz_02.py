"""
Question 2:
Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without
turning it into a dictionary. How do you skip over the header record with the field names?
"""

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = file.readlines()
    skipHeader = True
    # Process each row
    for row in rows:
        if skipHeader:
            skipHeader = False
            continue
        name, color, type = row.strip().split(",")

        # Format the return string for data rows only
        return_string += "a {} {} is {}\n".format(color, name, type)

  return return_string

#Call the function
print(contents_of_file("flowers.csv"))