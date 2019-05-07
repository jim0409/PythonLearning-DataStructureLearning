from enum import IntEnum

class Animal(IntEnum):
    DOG = 1
    CAT = 2
    PANDA = 3

globals().update(Animal.__members__)

print(DOG)
# Animal.DOG

print(DOG == 1)
# True

print(Animal(1))
# Animal.DOG