import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    # 因為要收的資料不是string，所以要宣告full_msg為bytes型別
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new message length: {}".format(msg[:HEADERSIZE]))
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        # full_msg += msg.decode('utf-8')
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print('full msg recvd')
            print(full_msg[HEADERSIZE:])

            # 使用pickle.loads把序列化的資料讀取出來
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    print(full_msg)
