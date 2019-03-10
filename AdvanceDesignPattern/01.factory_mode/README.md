# 工廠模式
1. 工廠方法(Factory Method)
    1. 應用場景：
        1. 軟體裡建立物件的程式碼散在各處，而不是由單一支函式/方法負責管控，以至於無法追蹤物件的建立過程。
    2. 實例：
        1. 某一支工廠方法負責連接到不同的資料庫(MySQL/SQLite)
    3. 優點：
        1. 降低記憶體用量：物件只會在需要時才會被創建及配置
    4. 範例:
        ```python
        class A(object):
            pass
        if __name__ == '__main__':
            a = A()
            b = A()

            print(id(a) == id(b))
            print(a, b)
        ```
2. 抽象工廠(Abstract Factory)
    1. 