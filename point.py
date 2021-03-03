class Point:
    def __init__(self, x=0, y=0):
        self.xy = (x, y)
    def __str__(self):
        return f'Point({self.xy[0]}, {self.xy[1]})'
    def __add__(self, other):
        a, b = self.xy
        c, d = other.xy
        return Point(a + c, b + d)



if __name__ == '__main__':
    origin = Point()
    point = Point(4, 1)
    other_point = Point(3, -3)
    third_point = point + other_point

    print(point)
    print(other_point)
    print(third_point)

    point += third_point
    print(point)
