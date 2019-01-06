# super()用於類別的繼承，調用父類別的一個方法


class A:
    pass


class B(A):
    def add(self, x):
        super().add(x)

