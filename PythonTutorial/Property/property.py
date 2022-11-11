# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # self.set_age(age)

#     def set_age(self, age):
#         if age <= 0:
#             raise ValueError('The age must be positive')
#         self._age = age  

#     def get_age(self):
#         return self._age     

#     age = property(fget = get_age, fset = set_age) 

# john = Person('John', 18)

# print(Person.age)

# print(john.__dict__)

# john.age = 19

# print(Person.__dict__)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age

#     def get_age(self):
#         return self._age

#     age = property(fget=get_age)

# john = Person('John', 25)
# print(john.age)    


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value

john = Person('John', 25)
print(john.age)  
print(john.__dict__)       