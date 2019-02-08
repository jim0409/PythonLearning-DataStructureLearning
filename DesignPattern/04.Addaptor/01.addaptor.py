class Dog:
    def speak(self):
        return 'woof'

    def __str__(self):
        return 'Dog'


class Cat:
    def speak(self):
        return 'meow'

    def __str__(self):
        return 'Cat'


class Adaptor:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


if __name__ == '__main__':
    objects = []
    dog = Dog()
    objects.append(Adaptor(dog, dict(make_noise=dog.speak)))

    for obj in objects:
        print(obj, obj.make_noise())
