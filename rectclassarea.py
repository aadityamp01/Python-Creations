class Rectangle:
    def __init__(self):
        self.length = float(input("Enter length of rectangle::"))
        self.width = float(input("Enter width of rectangle::"))

    def rectangle_area(self):
        return self.length*self.width

obj_Rectangle = Rectangle()
print('The area of rectangle is :',obj_Rectangle.rectangle_area())
