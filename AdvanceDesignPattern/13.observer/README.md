# 觀察者模式
當一個對象的狀態變動時需要通知其他很多對象的時候，通常搭配繼承來使用。

e.g.
當一個數據更新時，數據會有多個formater，formater會被通知到更新這個事件。

# 精神
會宣告，多個類似的Class，且每個Class都具有同樣，或是差不多的method可以呼叫。
在執行完main publisher的時候會再額外去跑一些notify。(其中notify可以是這些client_class裡面的method)

# observer01.py
### 觀察者模式架構:
DefaultFormater(發佈者關注事件，會需要繼承一個控制訂閱者的物件) -> Publisher(include observers：控制訂閱者的物件) -> HexFormatter(訂閱者), BinaryFormatter(訂閱者)

- Steps:
  1. 增加一個發佈者DefaultFormater(繼承Publisher)，並且賦予一個data的初始值"test1"
  2. 增加另一個訂閱者HexFormater()，並且把這個訂閱者加入“提醒通知”內。
  3. 更改預設的data值，在排查看看是否訂閱者的data值也有同步到。

# observer02.py
### 觀察者模式架構:
ClientQueue做做為一個收集事件的佇列。每當加入新的Client時，clients=[]以及listeners=[]都會append新的Subscriber，藉由定義ClienterLogger以及ClientFormater可以看到兩個Client的Listener。實作clientAdded, clientRemoved以及show這三個function，當ClientQueue有新增或是減少client都會做出通知(notify)


# refer
https://openhome.cc/Gossip/DesignPattern/ObserverPattern.htm