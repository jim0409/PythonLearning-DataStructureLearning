# -*- coding: UTF-8 -*-

import re

line1 = 'www'
line2 = 'www.runoob.com'

# print("method of match")
print("======method of match====")
# re.match嘗試從起始位置匹配一個模式
# 如果不是起始位置匹配成功的話match()就會返回none
# syntax: re.match(pattern, string, flags=0
print(re.match(line1, line2).span())
print(re.match("com", line2))

print(re.match(line1, line2).group())

line3 = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line3, re.M | re.I)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
else:
    print("No match")

# print("method of search")
print("======method of search====")
# re.search方法
# 掃描整個字符串並返回第一個成功的匹配
# syntax: re.search(pattern, string, flags=0)
print(re.search(line1, line2).span())
print(re.search("com", line2).span())

print(re.search(line1, line2).group())

searchObj = re.search(r'(.*) are (.*?) .*', line3, re.M | re.I)
if searchObj:
    print("searchObj.group(): ", searchObj.group())
    print("searchObj.group(1): ", searchObj.group(1))
    print("searchObj.group(2): ", searchObj.group(2))
else:
    print("No match")

# conclusion:
# re.match() 會從字串的頭開始進行匹配，如果字串開始不符合正規表達式，則匹配失敗。
# re.search() 則是會匹配整個字串，直到找到一個匹配
