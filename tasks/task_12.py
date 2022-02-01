import math
from sources import Point

class IncorrectTriangle(Exception):
    pass

def get_user_point(point_name):
    try:
        x, y = map(int, input(f'Enter {point_name}: ').strip().split(' '))
    except Exception:
        get_user_point(point_name)
    else:
        return Point(x,y)


class Triangle:

    def __init__(self, point_one, point_two, point_three):
        self.a = point_one
        self.b = point_two
        self.c = point_three
        if not self.a == self.b == self.c:
            raise IncorrectTriangle('Incorrect triangle')

        self.corners_set = ((self.a, self.b, self.c), (self.a, self.c, self.b), (self.b, self.a, self.c))

    def get_degree_from_three_coords(self, one: Point, two: Point, three: Point):
        x1 = one.x - two.x
        x2 = three.x - two.x
        y1 = one.y - two.y
        y2 = three.y - two.y
        d1 = pow(x1*x2 + y1* y1, 0.5)
        d2 = pow(x2* x2 + y2* y2, 0.5)
        return (math.acos((x1*x2+y1*y2)/(d1 * d2)))* 180 / math.pi


    def is_rectangular(self):
        for corner in self.corners_set:
            if self.get_degree_from_three_coords(*corner) == 90:
                return True
        return False

if __name__ == '__main__':
    one = get_user_point('one point')
    two = get_user_point('second point')
    three = get_user_point('third point')
    try:
        triangle = Triangle(one, two, three)
    except IncorrectTriangle as err:
        print(err)
    else:
        if triangle.is_rectangular():
            print('YES')
        else:
            print('NO')
