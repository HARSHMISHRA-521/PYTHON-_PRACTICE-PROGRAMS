class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # super().__init__(radius, radius)
                                                    #here this area cpould be calculated by two ways one is the
                                                   # coomented lines by ussing super()
    def area(self):
        # return f'The area is: { 3.14 * super().area()}'
        return f'The area is: { 3.14 * self.radius*self.radius}'



# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())