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


var = "text"
print(type(var))
print(dir(var))
print(help(''))

class Apple:
    pass

class Apple:
    """ Class that represents an apple """
    color = ""
    flavor = ''
    def __init__(self, color, flavor):
        """ constructor to set the initial values """
        self.color = color
        self.flavor = flavor
    def __str__(self):
        """ apple to String """
        return "Apple[color={}, flavor={}]".format(self.color, self.flavor)

formatNextTopic('Objects and apples')
apple = Apple("red", "sweet")
apple.color = "red"
apple.flavor = "sweet"
print('apple\'s color is {} and its flavor is {}'.format(apple.color, apple.flavor))


formatNextTopic('Instance methods')
class Piglet:
    name = "piglet"
    def speak(self):
        print("oik oik")

    def speak2(self):
        print('Oink! I am a {}! Oink!'.format(self.name))

p = Piglet()
p.speak()

p.name = "Hamlet"
p.speak2()

formatNextTopic('Constructors and STR functions')
a1 = Apple("Green", "Spicy")
print(a1)

formatNextTopic('Documenting classes')
help(Apple)


formatNextTopic("Working with an Elevator")

class Elevator:
    bottom = 0
    top = 0
    current = 0
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        return "Current floor: {}".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.current <= self.top and self.current >= self.bottom:
            self.current = floor

elevator = Elevator(-1, 10, 0)
elevator.up()
print("Current floor: " + str(elevator.current)) #should output 1

elevator.down()
print("Current floor: " + str(elevator.current)) #should output 0

elevator.go_to(10)
print("Current floor: " + str(elevator.current)) #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9

# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevattor)