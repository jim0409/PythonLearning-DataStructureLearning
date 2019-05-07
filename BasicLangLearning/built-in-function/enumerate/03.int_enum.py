import enum

class Shape(enum.IntEnum):
    SQUARE = 1
    CIRCLE = 2
    TRIANGLE = 3

print(Shape.SQUARE == 1)
# True

print(Shape.CIRCLE == 2)
# True

print(Shape.TRIANGLE == 3)
# Flase