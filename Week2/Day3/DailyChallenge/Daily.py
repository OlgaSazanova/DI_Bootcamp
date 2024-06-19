import math
#The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
class Circle:
    def __init__(self, radius : float = None, diameter: float = None) -> None:
        if radius is not None:
            self.radius - radius
            self.diameter = radius*2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter /2

        else:
            raise ValueError('Should be provided diameter or radius')
     # Compute the circle’s area   
    def circle_area(self):
        area= math.pi * math.pow(self.radius, 2)
        return area
    
# Print the attributes of the circle - use a dunder method
    def __str__(self) -> str:
        area = self.circle_area()
        return f"Circle's radius {self.radius}, diameter {circle.diameter} and area {area:.2f}"
    
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
    def __add__(self, other):

        return self.circle_area() > other.circle_area()
 
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
    def __gt__(self, other):
        return self.circle_area() > other.circle_area()
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
    def __eq__(self, other) -> bool:
        return self.radius == other.radius
# Be able to put them in a list and sort them
    def __lt__(self, other) -> list:
        return self.circle_area() < other.circle_area()
    

c1 = Circle(radius=13)
c2 = Circle(diameter=4)
c3 = Circle(radius=34)

print(c1)
print(c2)
print(c3)


c4 = c1+c2
print(c4)


print(c2 > c1) 
print(c2 == c3) 
print(c2 < c3)  

circles = []
circles = [c1, c2, c3, c4]
circles.sort()
for circle in circles:
    print(circle)