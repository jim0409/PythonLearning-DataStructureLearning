# re.compile(pattern[, flags])
# par:
#   pattern : 一個正規表達式
#   flags   : 可選，表示匹配模式，比如忽略大小寫，多行模式;
#       re.I 忽略大小寫
#       re.L 表示忽略特殊字符集\w, \W, \b, \B, \s, \S依賴於當前環境
#       re.M 多行模式
#       re.S 即為 . 並且包括換行符在內的任意字符( . 不包括換行符)
#       re.U 表示特殊字符集\w, \W, \b, \B, \d, \D, \s, \S依賴於Unicode字符屬性數據庫
#       re.X 為了增加可讀性，忽略空格和#後面的註釋

# -*- coding: UTF-8 -*-
import re

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)

m1 = pattern.match('one12twothree34four', 2, 10) # 從元素'e'開始匹配
print(m1)

m2 = pattern.match('one12twothree34four', 3, 10) # 從元素'1'開始匹配
print(m2)

print(m2.group(0))

print(m2.start(0))

print(m2.end(0))

print(m2.span(0))