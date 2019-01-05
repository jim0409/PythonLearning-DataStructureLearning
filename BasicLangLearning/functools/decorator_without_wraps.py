def logged(func):
    def with_logging(*args, **kwargs):
        """
        test with_logging
        """
        print(func.__name__+" was called ...")
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

# 因為使用裝飾法，所以f.__name__跟f.__doc__會返回裝飾法的name及doc
# f.__name__ 為 with_logging
# f.__doc__ 為 test_with_logging

print(f(2))

# f was called ...
# 6