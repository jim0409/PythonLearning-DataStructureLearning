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

# 雖然使用裝飾法，但是有加functools.wraps所以f.__name__跟f.__doc__會返回函數的name及doc
# f.__name__ 為 f
# f.__doc__ 為 test func f

print(f(2))

# f was called ...
# 6
