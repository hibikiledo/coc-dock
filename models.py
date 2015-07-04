__author__ = 'Hibiki'


'''
    Simple class for representing coordinate
    on screen
'''
class Point:

    def __init__(self, x, y):
        # cast input x and y to int
        self.x = int(x)
        self.y = int(y)

    def equals_to(self, other):
        return self.x == other.x and self.y == other.y

    def closes_to(self, other,  max_diff):
        for point in other:
            if abs(self.x - point.x) <= max_diff and abs(self.y - point.y) <= max_diff:
                return point
        return None

    def __str__(self):
        return ':'.join([str(self.x), str(self.y)])

