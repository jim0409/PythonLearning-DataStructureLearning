def check(func):
    def inside(a, b):
        if b == 0:
            print("Can't divide by 0")
            # return msg for error usage
            return "{}".format("please modify for another diver")

        return func(a, b)

    return inside


@check
def div(a, b):
    return a / b

print(div(10, 1))
print(div(10, 0))


def check2(func):
    def dummyfunc(a,b):
        if a >0 or b>0:
            print('a & b are {}.{}'.format(a,b))
            return '{} : a is {} & b is {}'.format("a and b are both postive numbers",a,b,)
        return func(a,b)
    return dummyfunc

@check2
def test(a,b):
    return 'a and b are {} {}'.format(a,b)

print(test(1,2))
# print('Test where a and b are {}.'.format(test(1,2)))