import functools

def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        """
        test with_logging
        """
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
    """
    test func f
    """
    return x+x*x

print("the f.__name__ is "+f.__name__)
print("the f.__doc__ is "+f.__doc__)
