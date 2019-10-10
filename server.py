import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname("socket22.herokuapp.com")

sock.bind((host,9090))

sock.listen(1)

conn, addr = sock.accept()

conn.send("lol".encode())

conn.close()
