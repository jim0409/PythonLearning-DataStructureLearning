def check(func):
    def inside(a, b):
        if b == 0:
            print "Can't divide by 0"
            # return msg for error usage
            return "{}".format("please modify for another diver")

        return func(a, b)

    return inside


@check
def div(a, b):
    return a / b


print div(10, 1)

print div(10, 0)

