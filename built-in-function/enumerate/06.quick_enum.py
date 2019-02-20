import enum
Animal = enum.Enum('Animal', 'CAT DOG PANDA')

print(Animal)
# <enum 'Animal'>

print("{} with value {}".format(Animal.CAT, Animal.CAT.value))
# Animal.CAT with value 1

print("{} with value {}".format(Animal.DOG, Animal.DOG.value))
# Animal.DOG with value 2

print("{} with value {}".format(Animal.PANDA, Animal.PANDA.value))
# Animal.PANDA with value 3
