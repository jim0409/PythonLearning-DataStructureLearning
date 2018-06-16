# 檢索和替換

# re.sub 提供了re.sub用於替換字串中的匹配項
# syntax: re.sub(pattern, repl, string, count=0, flags=0)
# par1:
#   pattern : 正則中的模式字符串
#   repl    : 替換的字符串，也可為一個函數
#   string  : 要被查找替換的原始字符串
#   count   : 模式匹配後替換的最大次數，默認0表示替換所有的匹配

# -*- coding: UTF-8 -*-
import re

phone = "2004-959-559 # 這是一個國外的電話號碼 ----- 4023985"

# 删除字符串中的 Python註釋
num = re.sub(r'#.*$', "", phone) # 找到有'#'的符號，後面的字串都會刪除
print("the phone number is: ", num)

# 删除非數字(-)的字符串
num = re.sub(r'\D', "", phone) # 只保留數字
print("the phone number is: ", num)

