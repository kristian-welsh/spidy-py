import socket

HOST = '127.0.0.1'
PORT = 9531
RESPONSE_BODY = """<html>
<head></head>
<body>
<marquee>hello!</marquee>
</body>
</html>"""
RESPONSE_HEAD = """HTTP/1.1 200 OK
Content-Length: {0}
Connection: close
""".format(len(RESPONSE_BODY))

class Responder:
    def process(self, request):
        return Response(RESPONSE_HEAD, RESPONSE_BODY)

class Router:
    def findResponder(self, request):
        return {
            "/": Responder()
        }[request.route()]

class Request:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def route(self):
        return "/"
    def method(self):
        return "GET"

class Response:
    def __init__(self, head, body):
        self.head = head
        self.body = body
    def __str__(self):
        return self.head + "\n" + self.body
    def code(self):
        return "200"

class Server:
    def __init__(self, host, port, router):
        self.host = host
        self.port = port
        self.router = router

    def run(self):
        with self.bindSocket() as s:
            s.listen()
            while True:
                self.acceptConnection(s)

    def bindSocket(self):
        theSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        theSocket.bind((self.host, self.port))
        return theSocket

    def acceptConnection(self, rootSocket):
        connection, address = rootSocket.accept()
        with connection:
            print('# incoming connection from: ', address)
            self.processConnection(connection)
            connection.close()
            print('# connection closed: ', address)

    def processConnection(self, connection):
        request = self.parseRequest(connection)
        response = self.generateResponse(request)
        self.sendResponse(response, connection)
        connection.close()
        print('## request: ', request)
        print('## response: ', response)

    def parseRequest(self, conn):
        total_data = ''

        print('recieving request')
        while '\r\n\r\n' not in total_data:
            data = conn.recv(2048)
            total_data += data.decode()
        print('request recieved')
        print(total_data)

        return Request(str(total_data))

    def generateResponse(self, request):
        responder = self.router.findResponder(request)
        response = responder.process(request)
        return response

    def sendResponse(self, response, connection):
        connection.sendall(bytearray(str(response), "UTF-8"))

Server(HOST, PORT, Router()).run()

