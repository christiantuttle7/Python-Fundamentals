import math
import copy

class Point:
    """ Point class represents and manipulates x,y coords. """

    count=0

    def __init__(self, x=3, y=4):
        """ Create a new point at x, y """
        Point.count += 1
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    # destructor 
    def __del__(self):
        Point.count -= 1

    def __add__(self, point):
        m  = Point()
        m.x = self.x + point.x
        m.y = self.y + point.y
        return m

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
        


def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

def distance(p1, p2):
    d = math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    return d



p = Point()         # Instantiate an object of type Point
q = Point(0,0)         # Make a second point


print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y
p.x = 1
p.y = 1
print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y
print("Distance = ", distance(p,q))
print("Distance from origin of p: ", p.distance_from_origin())
#print(p.to_string())

print(str(p))
print()
print(p.halfway(q))

r = Point(9,9)
print(Point.count)
r.__del__()
print(Point.count)

print()

rec = Rectangle(Point(1,2),2,3)
print(rec)
rec2 = rec
print(rec2 is rec)
rec2 = copy.copy(rec)
print(rec2)
rec.corner.x = 8
print(rec, rec2)

rec3 = copy.deepcopy(rec2)
rec.corner.x = 9
print(rec, rec3)

print(p, q)
print(q + p)
p.x = 9
print(p+q)




