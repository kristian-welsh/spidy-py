import socket
import model

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

    def parseRequest(self, connection):
        data = ''
        while not self.requestComplete(data):
            data += connection.recv(2048).decode()
        print('request recieved')
        print(data)
        return model.Request(data)

    def requestComplete(self, request):
        return '\r\n\r\n' in request or '\n\n' in request

    def generateResponse(self, request):
        responder = self.router.findResponder(request)
        response = responder.process(request)
        return response

    def sendResponse(self, response, connection):
        connection.sendall(bytearray(str(response), "UTF-8"))
        print('response sent:')
        print(str(response))

