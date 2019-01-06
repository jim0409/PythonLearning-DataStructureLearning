# compile()函數將一個字符串編譯為字節代碼
# syntax: compile(source, filename, mode[, flags[, dont_inherit]])
# 參數：
#   source -- 字符串或者AST(Abstract Syntax Trees)對象
#   filename -- 代碼文件名稱，如果不是從文件讀取代碼則傳遞一些可辨認的值
#   mode -- 指定帶把的種類。可以為exec, eval 或 single
#   flags -- 變量作用域，局部命名空間。如果被提供，可以是任何映射對象。
# 補充：
# flags和dont_inherent是用來控制編譯源碼時的標誌

str1 = "for i in range(0,10): print(i)"
c = compile(str1, '', 'exec') # 編譯為字節代碼對象
print(c)

exec(c)

str2 = "3 * 4 +5"
a = compile(str2, '', 'eval')
print(a)

print(eval(a))