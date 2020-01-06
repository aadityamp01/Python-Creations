# Python class named rectangle constructed by a length and width and a method which will compute the area of a rectangle.
# Creating a class rectangle

class rectangle():
    def __init__(self,width,length):  # initializing the attributes of the class
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length
    
a = int(input("Enter length of rectangle: "))
b = int(input("Enter width of rectangle: "))

obj = rectangle(a,b)             # Creating an instance a class

print("Area of rectangle: ",obj.area())     
 
