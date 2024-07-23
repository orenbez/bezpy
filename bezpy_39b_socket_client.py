
import pickle
import socket

HOST = '35.175.103.104' # Remote Host you wish to connect to
PORT = 7383
ADDR = (HOST,PORT)
BUFFSIZE = 1024 # bytes

# bytes('abc','utf-8') is the same as 'abc'.encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4, SOCK_STREAM = TCP
s.connect(ADDR)
qs = "12345678,2"  # query string
s.send(bytes(qs,'utf-8'))  # Sending string policy_number, vehicle_number to server
# ALTERNATIVELY use this to encode the string into bytes s.send(qs.encode('utf-8'))
# ALTERNATIVELY send a full python object like a dictionary (d) with s.send(pickle.dumps(d))
# ALTERNATIVELY send a full json string object (js) s.send(bytes(json.dumps(js), 'utf-8') (MORE GENERIC THAN PICKLE)

msg = s.recv(BUFFSIZE)
obj = s.recv(BUFFSIZE)
print('msg:', msg, type(msg))
print('msg.decode("utf-8"):', msg.decode('utf-8'), type(msg.decode('utf-8')))
print('obj:', obj, type(obj))
print('pickle.loads(obj)', pickle.loads(obj), type(pickle.loads(obj)))
s.close()



# simple html example

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('data.pr4e.org', 80))
s.send('GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode())

while True:
    data = s.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
s.close()

# HTTP/1.1 200 OK
# Date: Wed, 25 May 2022 03:06:32 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Mon, 15 May 2017 11:11:47 GMT
# ETag: "80-54f8e1f004857"
# Accept-Ranges: bytes
# Content-Length: 128
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/html
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://data.pr4e.org/page2.htm">
# Second Page</a>.
# </p>