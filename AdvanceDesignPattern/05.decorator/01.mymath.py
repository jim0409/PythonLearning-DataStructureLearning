import functools


def memoize(fn):
    known = dict()
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            print("remember the dict with args {}".format(args, known), end='\t')
            print("remember the dict with key {}".format(*args, known))
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize
def nsum(n):
    '''return 1+2+..+n'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@memoize
def fibonacci(n):
    '''return fib series n'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci', 'func': fibonacci}, {
        'exec': 'nsum(200)', 'import': 'nsum', 'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']),
                  'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: {}'.format(
            m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit()))
