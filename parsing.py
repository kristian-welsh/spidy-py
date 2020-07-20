from model import Request

def parse(data):
    parser = Parser('\r\n') if '\r\n' in data else Parser('\n')
    return parser.parse(data)

class Parser:
    def __init__(self, newL):
        self.newL = newL

    def parse(self, data):
        head, body = tuple(data.split(self.newL + self.newL))
        method, uri, protocol = self.firstLine(head).split(' ')
        headers = self.parseHeaders(head)
        return Request(data)

    def firstLine(self, head):
        return head.split(self.newL)[0]

    def parseHeaders(self, head):
        headers = head.split(self.newL)[1:]
        return dict([tuple(header.split(': ')) for header in headers])

