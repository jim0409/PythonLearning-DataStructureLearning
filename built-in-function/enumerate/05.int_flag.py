import enum
class Permission(enum.IntFlag):
    R = 4
    W = 2
    x = 1

print(Permission.R | Permission.W)

print(Permission.R + Permission.W)

RW = Permission.R | Permission.W

print(Permission.R in RW)