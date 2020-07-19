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

