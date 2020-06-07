# -*- coding: UTF-8 -*-

import hashlib
m = hashlib.md5()
data = "G. T. Wang"

# 先將資料編碼，再更新 MD5 雜湊值
m.update(data.encode("utf-8"))

h = m.hexdigest()
print(h)



# refer:
# Python“Non-ASCII character 'xe5' in file”报错问题
# - https://blog.csdn.net/geekmanong/article/details/50514984

# md5 for python
# https://blog.gtwang.org/programming/python-md5-sha-hash-functions-tutorial-examples/

# # 引入 hashlib 模組
# import hashlib

# # 建立 MD5 物件
# m = hashlib.md5()

# # 要計算 MD5 雜湊值的資料
# data = "G. T. Wang"

# # 更新 MD5 雜湊值
# m.update(data)

# # 取得 MD5 雜湊值
# h = m.hexdigest()
# print(h)
