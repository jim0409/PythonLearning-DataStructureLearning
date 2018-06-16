# 考慮repl參數是一個函數的情況

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'q(^(*+_341BA23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))