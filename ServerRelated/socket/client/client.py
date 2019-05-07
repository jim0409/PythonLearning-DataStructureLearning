import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',9999)) #連上剛剛設定的9999
while True:
    print (sock.recv(2048))