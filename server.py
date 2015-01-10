# -*- coding: utf-8 -*-
import SocketServer
import socket
import json

HOST = socket.gethostbyname('')
PORT = 4000

class Handler(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            json_data = self.request.recv(1024)
            if len(json_data) == 0:
                print("emp")
                break
            print(json_data)
            data = json.loads(json_data)
            res = ""
            res += "sn: " + data['twitterID']
            print(res)
            self.request.send(res)
        self.request.close()

server = SocketServer.TCPServer((HOST, PORT), Handler)
print 'listening', server.socket.getsockname()
server.serve_forever()
