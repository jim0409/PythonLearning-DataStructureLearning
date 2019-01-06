# complex(): 函數用於創建一個值為real+imag*j的複數，或轉化一個字符串或數字為複數。
# 如果第一個參數為字串，則不需要指定第二個參數。
# syntax: class complex([real[, imag]])
# 參數說明：
#   real -- int, long, float 或字符串
#   imag -- int, long, float
# 返回值：
#   返回一個複數

print(complex(1,2))

print(complex(1))

print(complex("1+2j"))