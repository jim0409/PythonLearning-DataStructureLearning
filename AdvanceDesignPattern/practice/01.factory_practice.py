class C1:
    def __init__(self, name):
        self.name = name
    def echo(self):
        print(self.name)

class C2:
    def __init__(self, name):
        self.name = name
    def echo(self):
        print(self.name)


if __name__ == '__main__':
    try:
        input_class = str(input("pleaes enter the class you want to use: "))
    except:
        print("enter must be string.")
    if input_class == 'c1':
        c = C1('class1')
    elif input_class == 'c2':
        c = C2('class2')
    else:
        print("Invalid class was entered.")

    c.echo()