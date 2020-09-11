inputValue = input("Please enter a number: ")
type(inputValue)
print("Type: " + str(type(inputValue)), inputValue)

# By using eval() function we can evaluate an expression from a string. Example
result = eval(inputValue)
t = type(result)
print("Result: ", result, ", Type of the expression: ", t)