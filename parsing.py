from model import Request

def parse(data):
    parser = Parser('\r\n') if '\r\n' in data else Parser('\n')
    return parser.parse(data)

class Parser:
    def __init__(self, newL):
        self.newL = newL

    def parse(self, data):
        head, body = tuple(data.split(self.newL + self.newL))
        request_line, header_strings = self.splitLines(head)
        method, uri, protocol = request_line.split(' ')
        headers = self.parseHeaders(header_strings)
        return Request(data)

    def splitLines(self, head):
        lines = head.split(self.newL)
        return (lines[0], lines[1:])

    def parseHeaders(self, headers):
        return dict([tuple(header.split(': ')) for header in headers])

