
import os
import socket
from xmlrpc.server import SimpleXMLRPCServer

#socket.gethostbyname("socket22.herokuapp.com")
host = ''
port = int(os.environ.get('PORT'))
print(port)




def is_even(n):
    return n % 2 == 0

server = SimpleXMLRPCServer((host, port))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()
