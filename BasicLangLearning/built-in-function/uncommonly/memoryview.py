# memoryview() 函數返回給定參數的內存查看對象(Memory view)
# 用法memoryview(view)

v = memoryview(bytearray('abcdef','utf-8'))
print(v)

print(v[1])

print(v[-1])

print(v[1:4])

print(v[1:4].tobytes())