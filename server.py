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

{0}""".format(responseBody, len(responseBody))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(2048)
			if not data:
				break;
			conn.sendall(bytearray(response, "UTF-8"))


