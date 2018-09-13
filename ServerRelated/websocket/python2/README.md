## Would build a WebSocket Server:
#### 4 import parts would be built
- writing a TCP/HTTP server to identify a websocket request
- Performing a handshake
- Decoding/ Receiving data/ frames
- Sending data/ frames

#### Writing A TCP/HTTP Server to Identify WebSocket Request
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

#### Performing a Handshake
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

#### Decoding an Incoming Frame
> 

... continue