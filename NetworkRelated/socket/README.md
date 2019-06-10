# 前言
Socket是程序間通訊的一種方式，他與其他程序奸凸訓的一個主要不同是。他能實現不同主機間的程序間通訊，我們每網路上各種各樣的服務大多都是基於Socket來完成通訊的，例如我們每天瀏覽網頁。line聊天，收發email等等。要解決網路上兩台主機之間的程序通訊問題，首先要唯一標示該程序，在TCP/IP網路協議中，就是通過(IP地址，協議，埠號)三元件來標示程序的，解決了程序標識問題，就有了通訊的基礎了。

TCP是一種面向連線的傳輸協議，TCP Socket是基於Client-Server的程式設計模型，服務端監聽客戶端的連線請求，一旦建立連線即可進行傳輸資料。那麼對TCP Socket程式設計的介紹也將區隔為`客戶端`以及`服務端`

# 練習socket server
1. TCP flow
```
Client -> Server: SYN
Server -> Client: SYN+ACK
Client -> Server: ACK
```
2. 測試server可用mz/ nc/ telnet/ curl 去觸發server TCP 反饋
3. 觀察packet可用netstat/ ss/ tcpdump/ wireshark 觀察包的發送狀況

# refer:
http://hhtucode.blogspot.com/2013/03/python-simple-socket-server.html
https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/369901/
https://docs.python.org/3/library/socket.html