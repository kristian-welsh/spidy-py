import model

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
        return model.Response(RESPONSE_HEAD, RESPONSE_BODY)

