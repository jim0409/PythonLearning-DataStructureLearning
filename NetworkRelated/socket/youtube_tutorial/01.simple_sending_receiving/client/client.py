import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


# recv 代表buffer，即每次socket接受的訊息量為多少
# 這邊設定1024，代表一次可以收到1024bits
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# 可以分片段收，每次收8bit，再將每次收到的8bit組合起來
full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
