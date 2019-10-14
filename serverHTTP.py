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
#

import http.server
import socketserver
import os


class MyClass(http.server.BaseHTTPRequestHandler):
    def on_GET(self):
        self.send_response(200)
        self.send_header("Contrent-type","text/html")
        self.end_headers()
        self.wfile.write("lol".encode())
    pass


def run(server_class=http.server.HTTPServer, handler_class= MyClass):
    PORT = int(os.environ.get('PORT'))
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)

    httpd.serve_forever()

if __name__ == "__main__":
    run()
