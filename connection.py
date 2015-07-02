import socket
import threading

HOST = '127.0.0.1'
PORT = 7711

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for res in socket.getaddrinfo(HOST, PORT, 0, socket.SOCK_STREAM):
    family, socktype, proto, caononame, socket_address = res
    print res
    s = socket.socket(family, socktype, proto)
    s.connect((HOST, PORT))

    try:
        s.send('ADDJOB queue2 ass 0')
        print "sent out, waiting for response"
        data = s.recv(1024)
        print "receive response"
        s.close()
        print 'Recieved'. repr(data)
    except socket.timeout:
        pass
    except socket.error:
        pass
    finally:
        s.close()
