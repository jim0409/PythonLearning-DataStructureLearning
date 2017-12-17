print("-----使用一般function--------")
#定義max函數
def max(a, b):
    return a if a > b else b
print(max(10, 20)) # 傳回 20

print("-----使用lambda語法--------")
#def max(a,b) 等同 lambda a, b: a if a > b else b
maxvalue = lambda a, b: a if a > b else b
print(maxvalue(10, 20)) # 傳回20

print("-----混和型lambda語法------")
#創造 混和不只一項判斷式
speciallambda=lambda a,b,c : a+b if a>b and b>c else a-b
print(speciallambda(5,4,3))
