# import socket
# port = 8000
#
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# host = socket.gethostbyname("")
#
# sock.bind((host,port))
#
#
# sock.listen(1)
# while True:
#
#     conn, addr = sock.accept()
#
#     conn.send("lol".encode())
#
#     conn.close()


#!flask/bin/python
from app import app

from flask import Flask
import os
app2 = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT'))

    app2.run(host = "0.0.0.0",port = PORT)
