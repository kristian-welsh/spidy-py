import socket

HOST = '127.0.0.1'
PORT = 8080
responseBody = """<html>
<head></head>
<body>
<marquee>hello!</marquee>
</body>
</html>"""
response = """HTTP/1.1 200 OK
Content-Length: {1}
Connection: close

{0}""".format(responseBody, len(responseBody))

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def listen(self):
        with self.bindSocket() as s:
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    self.respond(conn)
                    conn.close()

    def bindSocket(self):
        theSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        theSocket.bind((self.host, self.port))
        return theSocket

    def respond(self, conn):
        data = conn.recv(2048)
        conn.sendall(bytearray(response, "UTF-8"))


Server(HOST, PORT).listen()


