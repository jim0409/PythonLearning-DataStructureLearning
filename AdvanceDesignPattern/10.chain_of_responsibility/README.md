# Vespe Savikko
parent -> Widget -> Event

Main Window -> Widget
Msg Text -> Widget
SendDialog -> Widget

# 責任練筆記：
1. 製造一個事件的類別
2. 製造一個主要的物件進入口(也會成為第一個parent)
3. 製造其次以及剩下的class作為第二，第三以及第四進入口
4. 進入口如果找不到該方法，會向上找尋parent是否存在該方法，有則執行。否則回應parent的unhandle方法