# exec() 執行儲存在字符串，或文件中的Python語句，相比於eval, exec可以執行更複雜的Python代碼。

# 需要说明的是在 Python2 中exec不是函数，而是一个内置语句(statement)，但是Python2中有一个 execfile() 函数。
# 可以理解为 Python 3 把 exec 这个 statement 和 execfile() 函数的功能够整合到一个新的 exec() 函数中去了。

# syntax: exec(obj)
# 參數:
#   obj --- 要執行的表達式

exec('print("Hello World")')

exec("""
for i in range(5): print('{}'.format(i))
""")

print("______________")

x = 10
expr="""
z = 30
sum = x + y + z
print(sum)
"""

def func():
    y = 20
    exec(expr)
    exec(expr, {'x':1, 'y':2})
    exec(expr, {'x':1, 'y':2}, {'y':3, 'z':4})

func()