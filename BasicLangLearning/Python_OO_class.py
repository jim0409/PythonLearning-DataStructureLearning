#使用class類別
#定義__init__(self): 放置參數前需要先宣告出要使用的變數
#可以藉由在變數前面加入__ 將該宣告變數變成私有變數, 否則python內預設變數皆為公開變數
class Human():      #等同class Human(object):   只是object可以省略
    def __init__(self,h,w):
        self.__height=h
        self.__weight=w
    def BMI(self):
        return self.__weight/((self.__height/100)**2)

a = Human(h = 155, w = 48)
print(a.BMI())
#使用繼承, 將Human的物件沿用到Woman
#要注意, 如果要沿用父類別下的物件, 必須要宣告super().__init__(參數)
class Woman(Human):
    def __init__(self,h,w,name,blood,single):
        super().__init__(h,w)
        self.name = name
        self.blood = blood
        self.single = single

    def ShowDetail(self):
        print("name = {}, blood = {}, state = {}, BMI={}".format(self.name,self.blood,self.single,self.BMI()))

b = Woman(155,48,'bella','B','Single')
b.ShowDetail()