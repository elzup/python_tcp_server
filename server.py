# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import socketserver
    import socket
    import json

    from handles import handler
    from models import log_model

    HOST = socket.gethostbyname('')
    PORT = 4000

    def work(self):
        while True:
            json_data = self.request.recv(1024).strip()
            if len(json_data) == 0:
                print("emp")
                break
            if json_data.__class__.__name__ == "bytes":
                json_data = json_data.decode('UTF-8')
            print(json_data.__class__)
            print(json_data)
            data = json.loads(json_data)
            print(data)
            res = ""
            res += "sn: " + data['twitterID']
            print(res)
            self.request.send(res.encode('UTF-8'))
        self.request.close()

    handler.Handler.set_work(work)
    limit = 1
    while (limit < 10):
        limit += 1
        try:
            server = socketserver.TCPServer((HOST, PORT), handler.Handler)
            break
        except OSError:
            print("port: " + str(PORT) + " is userd")
            PORT += 1

    print('listening', server.socket.getsockname())
    server.serve_forever()
