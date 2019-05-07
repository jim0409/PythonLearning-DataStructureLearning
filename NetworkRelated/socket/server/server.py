import socket
import time

# socket起始參數
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('0.0.0.0', 9999))  # 自己可以設定什麼port，這裡我用9999
while True:
    server_sock.listen(0)
    client, address = server_sock.accept()
    print(address, "connected")
    while True:
        try:
            send_data = ",".join(["Hello", "Nice", "To", "meet", "you"])
            client.send(send_data)
        except:
            print(address, 'Closed')
            break
        time.sleep(5)
