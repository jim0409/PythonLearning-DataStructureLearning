# Python 裡面沒有 switch-case 的語法，所以你必須用其他的方式，來達到類似的功能。
# {}.get() 會根據 level 這個 key 傳回指定的 lambda 函式，如果找不到 key，則回傳回 get() 第二個引數裡面所設定的預設函式。

score = int ( input('please insert a number : '))
level = score // 10
{
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()
