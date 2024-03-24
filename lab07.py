import socket
import select
sockL = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = "10.0.2.103"   
port = 60003
sockL.bind((host, port))
sockL.listen(1)

ListOfSockets = [sockL]
print("Listening on port {}".format(port))

while True:
    tup = select.select(ListOfSockets, [], [])
    sock = tup[0][0]
    if sock == sockL: 
        client_host, client_port = sockL.accept()
        ListOfSockets.append(client_host)
        for i in range(1,len(ListOfSockets)):
            if ListOfSockets[i] != sock:
                ListOfSockets[i].sendall(bytearray("[{}] (Connected)".format(client_port),"ascii"))
            else:
                print("Unable to connect {}".format(client_port))
    else: 
        data = sock.recv(2048).decode()
        if not data:
            #client_host.sendall(bytearray("[{}] (Diconnected)".format(client_port),"ascii"))
            for i in range(1, len(ListOfSockets)):
                if ListOfSockets[i] != sock:
                    ListOfSockets[i].sendall(bytearray("[{}] (Diconnected)".format(client_port),"ascii"))
            sock.close()    
            for i in range(1, len(ListOfSockets)):
                if ListOfSockets[i] == sock: 
                    ListOfSockets.pop(i)
                    break
            
        else:
            for i in range(1,len(ListOfSockets)):
                ListOfSockets[i].sendall(bytearray(data,"ascii"))