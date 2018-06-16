# 和findall類似，在字符串中找到正則表達所匹配的所有字串，
# 並把它們作為一個迭代器返回
# syntax:
#   re.finditer(pattern, string, flags=0)

import re

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
