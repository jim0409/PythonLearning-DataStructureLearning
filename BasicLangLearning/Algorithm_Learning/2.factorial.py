def factorial(i):
    if i == 0:
        return 1
    else:
        # recursive function
        ans = i * factorial(i - 1)

    return ans


Nfactorial = int(input("please enter an int :"))
print(factorial(int(Nfactorial)))
