# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'({self.x},{self.y})'

#     def add(self, point):
#         if not isinstance(point, Point2D):
#             raise ValueError('The other must be an instance of the Point2D')

#         return Point2D(self.x + point.x, self.y + point.y)

#     def __add__(self, point):
#         if not isinstance(point, Point2D):
#             raise ValueError('The other must be an instance of the Point2D')
#         return Point2D(self.x + point.x, self.y + point.y)
#         # return (self.x + point.x, self.y + point.y)

# if __name__ == '__main__':
#     a = Point2D(10, 20)
#     b = Point2D(15, 25)
#     c = a.add(b)
#     print(c)
#     print(type(c))

#     c = a + b
#     print(c)
#     print(type(c))
#     # c = a.__add__(b)

class Item:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    @property
    def amount(self):
        return self.qty * self.price

    def __str__(self):
        return f'{self.name} {self.qty} ${self.price} ${self.amount}'

class Cart:
    def __init__(self):
        self.items = []

    def __iadd__(self, item):
        if not isinstance(item, Item):
            raise ValueError('The item must be an instance of Item')
        
        self.items.append(item)
        return self

    @property
    def total(self):
        return sum([item.amount for item in self.items])

    def __str__(self):
        if not self.items:
            return 'The cart is empty'

        return '\n'.join([str(item) for item in self.items])  

if __name__ == '__main__':
    cart = Cart()          

    cart += Item('Apple', 5, 2)
    cart += Item('Banana', 20, 1)
    cart += Item('Orange', 10, 1.5)

    print(cart)

    print('-' * 30)
    print('Total: $', cart.total)