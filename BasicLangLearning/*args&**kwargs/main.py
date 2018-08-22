a = {1: 1, 2: 2, 3: 3, 4: 4}

b = {'a1': 1, 'a2': 2}

test_enum = {
    'a1': 1,
    'a2': 2
}


def test(*args):
    return args


def test2(**kwargs):
    key = []
    value = []
    for i, j in kwargs.items():
        key.append(i)
        value.append(j)
    print key
    print value
    return key, value


print(test(a))
print test(b)

print("-----")
test2(key=a, value=b, index=b)
print("-----")
test2(**b)
print("-----")
test2(**test_enum)


# print("-----")
# test2(**a) # would return error since keywords must be strings


class testclass(object):
    def __init__(self, a1, a2):
        self.__a1 = a1
        self.__a2 = a2

    @staticmethod
    def print_test(test, test2):
        a = testclass(test, test2)
        print "the test a1 is {}, while the test a2 is {}".format(a.__a1, a.__a2)


# @staticmethod create method iff func is using
# e.g.
# testclass.print_test(1,2)

def verifytestclass(**kwargs):
    for i, j in kwargs.items():
        if i=='a1':
            print "the expect verify class -- 'i' : {} ; 'j : {}".format(i, j)
            testclass.print_test(i, j)


verifytestclass(**test_enum)
