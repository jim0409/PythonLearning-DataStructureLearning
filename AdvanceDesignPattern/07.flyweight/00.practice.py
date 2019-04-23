import random


class flyweight_practice:
    pool = dict()

    def __new__(cls, random_num):
        # 如果沒有拿到random_num就回傳None
        obj = cls.pool.get(random_num, None)
        if not obj:
            print('enter here because there did not exist num {}\n'.format(random_num))
            obj = object.__new__(cls)
            cls.pool[random_num] = obj
            obj.random_num = random_num
        return obj

    def return_render(self):
        return "the render value is {}".format(self.random_num)

    def print_render(self):
        print('the render random_num is {}\n'.format(self.random_num))


for i in range(0, 100):
    t1 = flyweight_practice(random.randint(0, 100))
    # t1.print_render()
    print("the render value is {}".format(t1.return_render()))


# 或許可以考慮統計，如何render可以render出最少的flyweight
# 或許要劃分每層的class，個別層再去做render
# render 包含 render，或許可以做分散式cache
"""
class flyweight1:
    pool1 = dict()

    def __new__(self, render_var1):
        obj = cls.pool1.get(render_var1, None)
        if not obj:
            obj = ojbect.__new__(cls)
            cls.pool1[render_var1] = obj
            obj.render_var1 = render_var1
        return obj
    
class flyweight2:
    pool2 = dict()

    def __new__(self, render_var2):
        obj = cls.pool2.get(render_var2, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool2[render_var2] = obj
            obj.render_var2 = render_var2
        return obj

class flyweight_render_pool(flyweight1, flyweight2):
    pool = dict()

    def __new__(self, render_vars):
        obj = cls.pool.get(render_vars, None)
        if not obj:
            if (cond1):
                obj = object.__new__(flyweight1(render_input))
                flyweight1.pool[render_vars] = obj
            elif (cond2):
                obj = object.__new__(flyweight2(render_input))
                flyweight2.pool[render_vars] = obj
            obj.render_vars = render_vars
        return obj
"""