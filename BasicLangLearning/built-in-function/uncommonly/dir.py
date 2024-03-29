# dir() 函數不帶參數時，返回當前範圍內的變量，方法和定義的類型列表;
# 帶參數時，返回參數的屬性，方法列表。
#   如果參數包含方法__dir__()，該方法將被調用。
#   如果參數不包含方法__dir__()，該方法將最大極限地收集參數信息。
# syntax: dir([object]) ; object -- 對象 變量 or 類型

print(dir()) # 獲得當前模組的屬性列表
print("_____________")
print(dir([])) # 查看列表的方法