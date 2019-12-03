# Python program to check a triangle is equilateral, isosceles or scalene.
# defining a function to check 
def check_triangle(x,y,z):
    if((x == 60 and y == 60 and z == 60) == 180):
        print("It is an equilateral triangle")

    elif((x == y or y == z or x == z) == 180):
        print("It is an isosceles triangle")


    elif(x != y != z <= 180):
        print("It is scalene triangle")

    else:
        print("It is not a triangle")


x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
print(check_triangle(x,y,z))


    

    





