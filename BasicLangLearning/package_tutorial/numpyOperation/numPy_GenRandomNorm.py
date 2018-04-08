import numpy as np

mu, sigma = 60, 15 #平均數及標準差
s = np.random.normal(mu, sigma, 100)  #產生100個平均=60, 標準差=15的成績
print(s)

b=s.astype(int)  #轉成int
b=b.clip(0, 100) #大於100者, 變成100; 小於0者, 變成0
print(b)

