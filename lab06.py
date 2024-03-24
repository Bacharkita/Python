#!/usr/bin/env python
import socket
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = ''   
port = 8080
sock.bind((host, port))
sock.listen(1)    
print("Listening ...")
while True:
    client_host, client_port = sock.accept()
    data = client_host.recv(1024).decode()
    print(data)
    #client_host.sendall(bytearray('<html><head>  </head><body> <h1> Your Browser sent the following request: </h1> <pre> {} </pre></body></html>'.format(data),"ascii"))
    response = """HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {}

<html>
<head></head>
<body>
    <h1>Your Browser sent the following request:</h1>
    <pre>{}</pre>
</body>
</html>
""".format(len(data), data)

    client_host.sendall(response.encode("utf-8"))
    client_host.close()
sock.close()

