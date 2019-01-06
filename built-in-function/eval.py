# eval()函數用來執行一個字符串表達式，並返回表達式的值
# syntax: eval(expression[, globals[, locals]])
# 參數：
#   expression -- 表達式
#   globals -- 變量作用域，全局命名空間，如果被提供，則必須是一個字典對象
#   locals -- 變量作用域，局部命名空間，如果被提供，可以是任何映射對象
# 返回值
#   返回表達式計算結果

import subprocess

x = 7

str1 = '3*x'
print(eval(str1))

str2 = 'pow(2,2)'
print(eval(str2))

str4 = 'print(cmd)'
eval(str4,{'cmd':'hostname'})

# for more reference
# http: // www.cnblogs.com/yyds/p/6276746.html
