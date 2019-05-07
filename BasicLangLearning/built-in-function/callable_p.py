class C:
    @classmethod
    def f(cls, *kwargs):
        print(*kwargs)


a = C()
print(callable(a))

print(callable(a.f))

print(C.f(a, 1))
