class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)

print(john == jane)
print(john is jane)

print(john == 20)
