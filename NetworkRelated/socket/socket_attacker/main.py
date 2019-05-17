
# 程式碼等待解決

import time
import socket
import struct

HOST = '127.0.0.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(88)

struct_tcp_info = struct.Struct('7B 24I')

#include <sys/types.h>
#include <sys/socket.h>

# while True
    # buf = s.getsockopt(socket.IPPROTO_TCP, socket.)



## refer
# https://www.douban.com/note/178129553/