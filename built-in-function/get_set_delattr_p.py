# 宣告一個新的類
class A(object):
    bar = 1
    bar_dict = { "k1":"v1" }
    bar_list = ['l1','l2']

# 以該類產生一個新的類資料結構
a = A()

# 透過get attribute拿到a下物件bar的值，b=5
b = getattr(a, 'bar')
print("check the value of b is {}".format(b))

# 重新定義a下面物件bar的值，並不會改變b的數值。表示b是透過copy拿到值的
setattr(a, 'bar', 5)

print("Now, a.bar would be {}".format(a.bar))
print("That being said, b wouldn't be effected {}".format(b))

# 刪除a下面物件deletebar後確認值是否存在
print("Before delete obj bar a.bar: {}".format(a.bar))

delattr(a, 'bar')
print("After deleting obj bar a.bar: {}".format(a.bar))

# also available to dict or list
c = getattr(a, 'bar_dict')
print("assume the bar_dict would be {}".format(c))
for i in c.keys():
    print(i, c[i])

d = getattr(a, 'bar_list')
print("assume the bar_list would be {}".format(d))
for i in range(len(d)):
    print(i, d[i])