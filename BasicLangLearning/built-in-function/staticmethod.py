# python staticmethod返回函數的靜態方法。該方法不強制要求傳遞參數
# e.g.
# class C(object):
#   @staticmethod
#   def f(arg1, arg2, ...)
#     ...
# 以上實力聲明了靜態方法f，類可以不用被產生就可以調用該方法。C.f()，當然在該類下的成員也可以調用其方法。


class C(object):
    @staticmethod
    def f():
        print('runoob')

C.f()

objc = C()
objc.f()