import re

# 編譯成 Pattern 對象
pattern = re.compile(r'hello')

# 取得匹配結果，無法匹配返回 None
match = pattern.match('hello world!')

if match:
    # 得到匹配結果
    print(match.group())




