# All the words come from 
> https://superuser.blog/websocket-server-python/
## Would build a WebSocket Server:
#### 4 import parts would be built
- writing a TCP/HTTP server to identify a websocket request
- Performing a handshake
- Decoding/ Receiving data/ frames
- Sending data/ frames

#### 1. Writing A TCP/HTTP Server to Identify WebSocket Request
> via python's SocketServer library to provide simple TCP server.
- the client would send an HTTP request which looks something like
```angular2html
GET /chat HTTP/1.1
Host: example.com:8000
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```
The request of type include three headers 
- Upgrade: websocket
- Connection: Upgrade
- Sec-WebSocket-Key: \ 

#### 2. Performing a Handshake
> need to send specific HTTP response back to client to establish the bidirecitonal connection.
- the response would look something like this
```angular2html
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```
via header Sec-WebSocket-Accept with value SHA1 of the key
- Sec-WebSocket-Accept: 
> As per protocol, you concatenate the key you received in request header (‘dGhlIHNhb…’) and the magic string (“258EAFA5-E914-47DA-95CA-C5AB0DC85B11”) , calcualte SHA1 hash of them and send back the base64 encoding of the hash (which is ‘s3pPLMB…’) 

#### 3. Decoding an Incoming Frame
> After the connection is established, client/the other side can send data to server.
However, the data wouldn't be in plain-text. it is using a special frame format defined in protocol.
```angularjs
      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
     +-+-+-+-+-------+-+-------------+-------------------------------+
     |F|R|R|R| opcode|M| Payload len |    Extended payload length    |
     |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
     |N|V|V|V|       |S|             |   (if payload len==126/127)   |
     | |1|2|3|       |K|             |                               |
     +-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
     |     Extended payload length continued, if payload len == 127  |
     + - - - - - - - - - - - - - - - +-------------------------------+
     |                               |Masking-key, if MASK set to 1  |
     +-------------------------------+-------------------------------+
     | Masking-key (continued)       |          Payload Data         |
     +-------------------------------- - - - - - - - - - - - - - - - +
     :                     Payload Data continued ...                :
     + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
     |                     Payload Data continued ...                |
     +---------------------------------------------------------------+
```
To read the payload data, you must know when to stop reading. That’s why the payload length is important to know. Unfortunately, this is somewhat complicated. To read it, follow these steps:
- Read bits 9-15 (inclusive) and interpret that as an unsigned integer. If it’s 125 or less, then that’s the length; you’re done. If it’s 126, go to step 2. If it’s 127, go to step 3.
- Read the next 16 bits and interpret those as an unsigned integer. You’re done.
- Read the next 64 bits and interpret those as an unsigned integer (The most significant bit MUST be 0). You’re done.
> Assuming payload data is less than 125 so that leave 2 to 6 as masking bytes.
```
1. send frame as byte array.
2. subtracting 128 (the mask bit) from byte 1.
3. encrypted payload XORed with the mask should give us the decrypted payload.
```

#### 4. Sending Frames
> Send data unmasked i.e. in plain text.
`where leave FIN bit, the OPCODE, the LEN and finally the payload`

## finally :
> make whole on roll and execute, then open browser to check it!
```javascript
ss =new WebSocket("ws://localhost:9999")

ss.onmessage = function(event)
{console.log(event.data);};

ss.send('I have high ground')
```