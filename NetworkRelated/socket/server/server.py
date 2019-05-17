import socket
import time

# socket起始參數
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('0.0.0.0', 10000))  # 自己可以設定什麼port，這裡我用9999
while True:
    server_sock.listen(0)
    client, address = server_sock.accept()
    print(address, "connected\n")
    # while True:
        # try:
    send_data = "hello nice to meet you\n"
        # 如果沒有轉send_data為bytes會噴錯，TypeError: a bytes-like object is required, not 'str'
    client.send(bytes(send_data, 'utf-8'))
        # time.sleep(5)
        # client.close()
    # server_sock.close()
    client.close()
    print(address, "closed\n")
