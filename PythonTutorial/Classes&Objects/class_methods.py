class Person:
    
    counter = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.counter += 1
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi I'm {self.first_name} {self.last_name}. I'm {self.age} years old."

    @classmethod
    def create_anonymous(cls):
        # cls.counter += 1
        return Person('John', 'Doe', 25)

p1 = Person.create_anonymous()        
# print(p1.introduce())
print(p1.counter)

print(p1.get_full_name())

p2 = Person('John', 'Deer', 27)        
# print(p2.introduce())
print(p2.counter)

p3 = Person('John', 'Doherty', 30)        
# print(p3.introduce())
print(p3.counter)