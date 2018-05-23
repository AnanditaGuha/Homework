class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

p = Point()         # Instantiate an object of type Point
q = Point(5,10)         # Make a second point
p.x = 4
p.y = 8
print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y
print("(x={0}, y={1})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y

print(p.y)
x = p.x
print(x)

print("(x={0}, y={1})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y

p = Point()
p.x = 7
p.y = 6

class Point:
    """ Point class represents and manipulates x,y coords. """

