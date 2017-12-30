import numpy as np
x =np.random.normal(size=5)
# 數據轉型 http://www.lianzai.me/article/285.html
y=(x>0).astype(np.float)

print(x)
print(y)

# 利用numpy的newaxis轉變矩陣的形狀 http://ben-do.github.io/2016/09/15/change-shape-of-matrix-by-numpy/
# print(x[:,np.newaxis])

# 將-5到10之間的數列等分成300個數字
# X_test = np.linspace(-5, 10, 300)
# print(X_test)

# numpy.ravel()
# http://blog.csdn.net/lanchunhui/article/details/50354978

x = np.array([[1,2],[3,4]])
print(x)
print(x.flatten())
print(x.ravel())  # 兩者均默認是行序優先

print("-----------改為列優先---------")
print(x.flatten('F'))
print(x.ravel('F'))  # 如此則默認為列序優先

print("-----------或者可以用reshape來調整矩陣-----")
print(x.reshape(-1))
print(x.T.reshape(-1))

print("--------flatten vs revel--------------")
x2 = np.array([[1,2],[3,4]])
x2.flatten()[1]=100  # flatten 返回的是拷貝，call by value
print(x2)

x2.ravel()[1]=99  # ravel 返回的是address，call by address
print(x2)
