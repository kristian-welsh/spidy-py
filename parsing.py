from model import Request


def parse(data):
    newL = '\r\n' if '\r\n' in data else '\n'
    return Parser(newL).parse(data)


class Parser:

    def __init__(self, newL):
        self.newL = newL

    def parse(self, data):
        head, body = tuple(data.split(self.newL + self.newL))
        method, uri, protocol, headers = self.parseHead(head)
        return Request(data)

    def parseHead(self, head):
        request_line, header_lines = self.splitLines(head)
        method, uri, protocol = request_line.split(' ')
        headers = self.parseHeaders(header_lines)
        return (method, uri, protocol, headers)

    def splitLines(self, head):
        lines = head.split(self.newL)
        return (lines[0], lines[1:])

    def parseHeaders(self, headers):
        return dict([tuple(header.split(': ')) for header in headers])
