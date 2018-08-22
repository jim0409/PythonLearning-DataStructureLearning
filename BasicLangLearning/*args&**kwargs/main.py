a = {1: 1, 2: 2, 3: 3, 4: 4}

b = {'a1': 1, 'a2': 2}

test_enum = {
    'a1': 1,
    'a2': 2
}


def test(*args):
    return args


def test2(**kwargs):
    for i, j in kwargs.items():
        print i, j
    return 0


# print(test(a))
print test(b)

print("-----")
test2(key=a, value=b, index=b)
print("-----")
test2(**b)
print("-----")
test2(**test_enum)
# print("-----")
# test2(**a) # would return error since keywords must be strings
