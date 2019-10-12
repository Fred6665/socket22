
import os
import socket
import psycopg2
from xmlrpc.server import SimpleXMLRPCServer

#socket.gethostbyname("socket22.herokuapp.com")
host = ''
port = int(os.environ.get('PORT'))
print(port)




def is_even(n):
    return n % 2 == 0

def print_lol():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    cursor = conn.cursor()
    cursor.execute("select * from lol")
    records =  cursor.fetchall()
    cursor.close()
    conn.close()
    return records

server = SimpleXMLRPCServer((host, port))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.register_function(print_lol, "print_lol")
server.serve_forever()
