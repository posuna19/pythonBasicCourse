import random
import datetime

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

formatNextTopic('Working with Random numbers')
print(random.randint(1,10))


formatNextTopic('Working with Dates')
now = datetime.datetime.now()
print(str(type(now)))
print(now)
print(now.year)

print(str(now + datetime.timedelta(days=14)))

""" 
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""