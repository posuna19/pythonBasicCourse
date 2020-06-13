print('while loop')
x = 0
while x < 5:
    print('Not yet, x is equals to ' + str(x))
    x = x + 1
print('x value is ' + str(x))
print()


#for loop
print("For loop:")
for x in range(5):
    print(x)
print()

print("List of friends:")
friends = ["Pedro", "Carmen", "Daniel"]
for friend in friends:
    print(friend)

# for with range function with 3 parameters
print()
print("for with range function with 3 parameters:")
for x in range(1,10,2):
    print(x)

print()
# Nested loops
print('Nested loops')
for left in range(7):
    for right in range(left, 7):
        print('[' + str(left) + '|' + str(right) + ']', end=' ')
    print()



print()
# Nested loops 2
print('Nested loops 2')
teams = ["Maverics","Bulls","Yankis","Stars"]
for homeTeams in teams:
    for awayTeams in teams:
        if homeTeams != awayTeams :
            print(homeTeams + ' VS ' + awayTeams)

print()
print()
for x in range(1, 10, 3):
    print(x)