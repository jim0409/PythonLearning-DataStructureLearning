# hasattr()用於判斷對象是否包含對應的屬性

#!/bin/bash

class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()
print(hasattr(point1, 'x')) # True
print(hasattr(point1, 'y')) # True
print(hasattr(point1, 'z')) # True
print(hasattr(point1, 'no')) # False
