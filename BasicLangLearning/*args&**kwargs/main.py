a = {1: 1, 2: 2, 3: 3, 4: 4}


def test(*args):
    return args

def test2(**kwargs):
    return kwargs

print(test(a))

# print(test2(a))