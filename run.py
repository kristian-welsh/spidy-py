from server import Server
from router import Router

HOST = '127.0.0.1'
PORT = 9531

Server(HOST, PORT, Router()).run()
