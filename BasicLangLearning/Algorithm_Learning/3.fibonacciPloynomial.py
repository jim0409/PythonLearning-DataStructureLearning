def fib(i):
    if i < 0:
        raise ValueError("Must be a positive integer.")
    if i == 0:
        return 0
    if i == 1 or i == 2:
        return 1
    if i >= 3:
        return (fib(i - 1) + fib(i - 2))


num1 = int(input("Please enter an integer: "))
for i in range(num1 + 1):
    print('fib(%d)=%d' % (i, fib(i)))
