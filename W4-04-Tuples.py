def formatNextTopic(title):
    formatedTitle = "***** " + title + " ****"
    totalLength = len(formatedTitle)
    separator = ""

    for x in range(totalLength):
        separator += '*'

    print()
    print(separator)
    print(formatedTitle)
    print(separator)


def getTime(seconds):
    hours = seconds // 60 // 60
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = (seconds - hours*3600 - minutes*60)
    return hours, minutes, remaining_seconds


"""
As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, 
and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type 
is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples 
are immutable. They’re specified using parentheses instead of square brackets.

You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful 
when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, 
the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, 
the position of the element in a tuple can have meaning. A good example of this is when a function returns 
multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. 
The order of the returned values is important, and a tuple ensures that the order isn’t going to change. 
Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple 
returned values from a function and store each value in its own variable.
"""


formatNextTopic("Tuples")
results = getTime(5000)
print(type(results))
print(results)
hours, mins, secs = results
print(hours, mins, secs)

tupleExample = ("summare.txt", "1025")
print(tupleExample)

formatNextTopic("Tuples and lists with enumarate")
names = ["Joe", "Bety", "Miriam"]
for i , name in enumerate(names):
        print("{} - {}.".format(i, name))


formatNextTopic("Tuples in an array")
def guest_list(guests):
	for name, age, job in guests:
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])