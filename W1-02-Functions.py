print(type("text"))
print(type(2))
print(type(3.5))
print("\n")

#Definition of a function
def greeting(name, department):
    print("Welcome, " + name)
    print("Your department is: "  + department)

greeting("Pedro", 'IT')
greeting("Nadia", 'Finance')
print("\n")

#Definition of a function with return
def triangle_area(base, height):
    return (base * height) / 2

area = str(triangle_area(5,8))
print('Triangle Area is:' + area)
print("\n")

def getTime(seconds):
    hours = seconds // 60 // 60
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = (seconds - hours*3600 - minutes*60)

    return hours, minutes, remaining_seconds

print('\nMultiples return values in a function:')
hours, minutes, seconds = getTime(7899)
print(hours, minutes, seconds)

