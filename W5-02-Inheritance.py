class Fruit:
    color = ""
    flavor = ''

    def __init__(self, name, other):
        """It initalizes the object with a name"""
        self.name = name
        self.other = other
    def __str__(self):
        print("isotherSet: " + str(len(self.other)>0))
        return "Fruit[color: {}, flavor: {}]".format(self.color, self.flavor)

    def color(self, color):
        """Sets the color of the fruit"""
        self.color = color

    def flavor(self, flavor):
        """Sets the flavor of the fruit"""
        self.flavor = flavor


class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

apple = Apple("Golden red", "other2")
apple.color("red")
apple.flavor('sweet')
print(apple)
