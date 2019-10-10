import socket
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname("socket22.herokuapp.com")
port = int(os.environ.get('PORT'))
sock.bind((host,port))

sock.listen(1)

while True:

    conn, addr = sock.accept()

    conn.send("lol".encode())

    conn.close()

