# Creating the file in mode w
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
guests.close()

# Reading the lines of the file
with open("guests.txt") as guests:
    for line in guests:
        print(line.strip())

# Appending text to the file
new_guests = ["Sam", "Danielle", "Jacob"]
with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")
guests.close()

print("********************************")
# Reading the new content of the file
with open("guests.txt") as guests:
    for line in guests:
        print(line.strip())


# Updating the file with the lastest guests, checked_out guest are removed from the file
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")
print("********************************")
# Reading the file
with open("guests.txt") as guests:
    for line in guests:
        print(line)
guests.close()


# Validating if some guest are in the hotel
print("********************************")
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for guest in guests:
        checked_in.append(guest.strip())
    for guest_to_check in guests_to_check:
        if guest_to_check in checked_in:
            print("{} is checked in".format(guest_to_check))
        else:
            print("{} is not checked in".format(guest_to_check))

