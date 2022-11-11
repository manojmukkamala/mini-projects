class Person:
    counter = 0
    version = 1

    def __init__(self, name, age):
        ### To define and initialize an attribute for all instances of a class, we use the __init__ method ###
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi {self.name}"

    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)

#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#---------- Object Oriented Programming ----------# 

# print(Person.counter)
# Person.counter = 10
# q = Person('Jane', 22)
# print(Person.counter)

# anonymous = Person.create_anonymous()
# print(anonymous.name)

# print(p.create_anonymous().name)       

#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#---------- Class ----------# 

# p = Person('John', 25)
# print(p)
# print(id(p))
# print(hex(id(p)))
# print(isinstance(p, Person))

#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#---------- Class Variables ----------#

# print(Person.__name__)
# print(type(Person))

# print(isinstance(Person, type))

# print(Person.counter)
# print(Person.version)
# print(Person.c)

# print(getattr(Person, 'counter'))
# print(getattr(Person, 'version'))
# print(getattr(Person, 'x', 10))

# setattr(Person, 'version', 2)
# print(Person.version)

# setattr(Person, 'x', 10)
# print(Person.x)

# delattr(Person, 'x')
# print(Person.x)

# from pprint import pprint
# pprint(Person.__dict__)

# print(Person.__dict__['counter'])

#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#---------- Instance Methods ----------#

# print(Person.greet)
# print(type(Person.greet))

p = Person('John', 25)
# print(p.greet)
print(type(p.greet))

# print(type(Person.greet) is type(p.greet))

# print(type(p.__dict__))


#----------#----------#----------#----------#----------#----------#----------#----------#----------#

# print("jupyter notebook --no-browser --ip 0.0.0.0 --allow-root")