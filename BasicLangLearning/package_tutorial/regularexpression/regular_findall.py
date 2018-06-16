# 在字串中找到正則表達式所匹配的所有字串，並返回一個列表。
# 如果沒有找到匹配的，則返回空列表
# syntax:
#   findall(string[, pos[, endpos]])
# par:
#   string  : 待匹配的字符串
#   pos     : 可選參數，指定字符串的起始位置，默認為0
#   endpos  : 可選參數，指定字符串的結束位置，默認字符串的長度。

import re

pattern = re.compile(r'\d+')  # 查找數字

result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
