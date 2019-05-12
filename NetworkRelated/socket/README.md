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