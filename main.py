class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def cal(point, p2):
        return point + p2


p = Point(3, 4)
p = Point(1, 4)
Point.cal(1, 3)

