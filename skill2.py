class Rectangle:
    def __init__(self, len, bre):
        self.len = len
        self.bre = bre
        def display(self):
            print("Length of Rectangle is: ", self.len)
            print("Breadth of Rectangle is: ", self.bre)
    def area(self):
        return (self.len * self.bre)

    def perimeter(self):
        return (2 * self.len + 2 * self.bre)


l = int(input("Enter  length :"))
b = int(input("Enter breadth  "))

r1 = Rectangle(3, b)

r1.display()

print("Area : ", r1.area())
print(" Perimeter: ", r1.perimeter())

class circle:
    def __init__(self, radius):
        self.radius = radius

    def __display__(self):
        print("Radius is: ", self.radius)

    def area(self):
        return (3.14 * self.radius * self.radius)

    def perimeter(self):
        return (2 * self.radius * 3.14)


r = int(input("Enter  Radius :"))

r1 = circle(r)

r1.display()

print("Area : ", r1.area())

print(" Perimeter: ", r1.perimeter())


class triangle:
    def __findPerimeter__(self, s1, s2, s3):
        return (s1 + s2 + s3)

    def findArea(self, s1, s2, s3):
        p = (s1 + s2 + s3)
        s = p / 2
        return (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5


s1 = float(input("first side : "))
s2 = float(input(" second side  : "))
s3 = float(input(" third side : "))

u = triangle()

print(" perimeter : {0:.2f}".format(
    u.findPerimeter(s1, s2, s3)))
print(" area  is : {0:.2f}".format(u.findArea(s1, s2, s3)))