# print("Hello, World!")

class Circle:
    """
    Circle class has 2 attributes: pi and radius
    Circle class has 2 methods: area and circumference

    pi and radius are called instance attributes. They belong to a specific instance of a class.
    """
    def __init__(self, radius):
        self.pi = 3.14159
        self.radius = radius
        print("New Circle Formed using Circle class")

    def area(self):
        return self.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.pi * self.radius

# c= Circle(5)        

class Circle2:
    """
    Circle2 has a class attribute: pi
    class attributes are placed outside of the __init__()
    class attributes can accessed via the instances of the class or via the class name
    """        
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        print("New Circle Formed using Circle2 class")

    def area(self):
        return self.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.pi * self.radius

# c= Circle2(5)

# print(c.pi)
# print(Circle2.pi)

# print(Circle.pi)

class Test:
    x = 10

    def __init__(self):
        self.x = 20

test = Test()

# print(test.x)
# print(Test.x)

class Circle3:
    circle_list = []
    counter = 0
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        self.circle_list.append(self)
        Circle3.counter += 1

c1 = Circle3(10)
print(c1.circle_list)

c2 = Circle3(20)
print(Circle3.circle_list)

print(Circle3.counter)