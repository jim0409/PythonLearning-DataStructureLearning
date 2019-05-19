import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    # 製造一個dict資料結構
    d = {1:'Hey', 2:'There'}
    # 使用pickle.dumps把dict資料序列化
    msg = pickle.dumps(d)

    # 將序列化後的資料送出
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    clientsocket.send(bytes(msg))
    # clientsocket.close()

