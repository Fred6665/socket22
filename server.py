
import os
import socket
from xmlrpc.server import SimpleXMLRPCServer


host = socket.gethostbyname("socket22.herokuapp.com")
print(os.environ.get('PORT'))





def is_even(n):
    return n % 2 == 0

server = SimpleXMLRPCServer((host, port))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()
