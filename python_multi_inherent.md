# python 處理多重繼承相關參考
# 範例 1. 改寫繼承的物件
子類別 (subclass) 繼承父類別 (superclass) 之後，子類別會得到父類別的所有方法 (method) 跟屬性 (attribute) ，這時候子類別只要重新定義跟父類別相同識別字 (identifier) 的方法，就會改寫 (override) 父類別原先定義的方法。

先來看到 __init__() 方法的改寫， Demo2 繼承自 Demo ， Demo2 重新定義了 __init__() 方法，因此在建立 Demo2 物件 (object) 實體 (instance) 的時候，會執行 Demo2 的 __init__() 方法

```python
class Demo:
    def __init__(self):
        print("demo")

class Demo2(Demo):
    def __init__(self):
        print("demo2")

d = Demo2()
```
===
result
```
$ python3 override01.py
demo2
$
```

# 範例2. 一般繼承物件的方式
如果希望先執行父類別的 __init__() 方法，就要用內建函數 (built-in function) super() 先行呼叫父類別的 __init__() 方法，例如這裡 Demo3 繼承自 Demo 類別， super() 方法在 __init__() 方法的第一行，因此建立 Demo3 的實體物件會先執行 Demo 的 __init__() 方法，然後才執行 Demo3 自己 __init__() 方法

```python
from override01 import Demo

class Demo3(Demo):
    def __init__(self):
        super().__init__()
        print("demo3")

d = Demo3()
```
===
result
```
$ python3 override02.py
demo2
demo
demo3
$
```

就一般的方法而言也是一樣的，這裡 Demo5 類別繼承自 Demo4 ，同樣兩者都有 demo() 方法， Demo4 的 demo() 方法先呼叫 super() 的 dmeo() 方法，因此 demo 字串 (string) 先於 subdemo 字串印出

```python
class Demo4:
    def demo(self):
        print("demo")

class Demo5(Demo4):
    def demo(self):
        super().demo()
        print("subdemo")

d = Demo5()
d.demo()

```
===
result
```
$ python3 override03.py
demo
subdemo
$

```

# 範例3. 多重繼承

最後來看看在多重繼承 (multiple inheritance) 下子類別方法的改寫，這裡 D4 類別繼承自 D1 、 D2 及 D3 類別， D4 的 __init__() 方法先用 super() 呼叫 __init__() 後，再個別以 D1 、 D2 及 D3 ，加上第二個參數 self 呼叫 __init__() 一次，這是由於 super() 的運作方式的原因，確保三個父類別的 __init__() 都會執行

```python
class D1:
    def __init__(self):
        print(1)

class D2:
    def __init__(self):
        print(2)

class D3:
    def __init__(self):
        print(3)

class D4(D1, D2, D3):
    def __init__(self):
        super().__init__()
        super(D1, self).__init__()
        super(D2, self).__init__()
        super(D3, self).__init__()
        print(4)

d = D4()
```
===
result
```
$ python3 override04.py
1
2
3
4
$
```


# refer 
# https://kaiching.org/pydoing/py/python-override.html